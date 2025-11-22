"""Thread-safe telnet client for Hargassner boiler."""
from __future__ import annotations

import asyncio
import logging
import socket
from asyncio import StreamReader, StreamWriter
from collections.abc import Callable
from datetime import datetime
from typing import Any

from ..const import (
    TELNET_BUFFER_SIZE,
    TELNET_MAX_RECONNECT_DELAY,
    TELNET_PORT,
    TELNET_RECONNECT_DELAY,
    TELNET_TIMEOUT,
)
from .message_parser import HargassnerMessageParser

_LOGGER = logging.getLogger(__name__)


class HargassnerTelnetClient:
    """Thread-safe telnet client with automatic reconnection."""

    def __init__(
        self,
        host: str,
        firmware_version: str,
        port: int = TELNET_PORT,
    ) -> None:
        """Initialize the telnet client.

        Args:
            host: IP address or hostname of the boiler
            firmware_version: Firmware version identifier (e.g., V14_1HAR_q1)
            port: Telnet port (default: 23)
        """
        self._host = host
        self._port = port
        self._firmware_version = firmware_version

        # Connection state
        self._reader: StreamReader | None = None
        self._writer: StreamWriter | None = None
        self._connected = False
        self._running = False

        # Background tasks
        self._receiver_task: asyncio.Task | None = None
        self._reconnect_delay = TELNET_RECONNECT_DELAY

        # Message parser
        self._parser = HargassnerMessageParser(firmware_version)

        # Data storage
        self._latest_data: dict[str, Any] = {}
        self._data_lock = asyncio.Lock()
        self._last_update: datetime | None = None

        # Statistics
        self._stats = {
            "messages_received": 0,
            "messages_parsed": 0,
            "parse_errors": 0,
            "reconnections": 0,
            "last_error": None,
        }

        # Callbacks
        self._data_callbacks: list[Callable[[dict[str, Any]], None]] = []

    async def async_start(self) -> None:
        """Start the telnet client and background receiver task."""
        if self._running:
            _LOGGER.warning("Telnet client already running")
            return

        _LOGGER.info("Starting telnet client for %s:%d", self._host, self._port)
        self._running = True

        # Start receiver task
        self._receiver_task = asyncio.create_task(self._receiver_loop())

        # Wait for initial connection
        for _ in range(50):  # 5 seconds max
            if self._connected:
                _LOGGER.info("Initial connection established")
                return
            await asyncio.sleep(0.1)

        _LOGGER.warning("Initial connection not established within timeout")

    async def async_stop(self) -> None:
        """Stop the telnet client and cleanup resources."""
        _LOGGER.info("Stopping telnet client")
        self._running = False

        # Cancel receiver task
        if self._receiver_task and not self._receiver_task.done():
            self._receiver_task.cancel()
            try:
                await self._receiver_task
            except asyncio.CancelledError:
                pass

        # Close connection
        await self._close_connection()

    async def _receiver_loop(self) -> None:
        """Background loop that receives and processes telnet messages."""
        while self._running:
            try:
                # Ensure connection
                if not self._connected:
                    await self._connect()

                # Read data
                if self._reader:
                    try:
                        data = await asyncio.wait_for(
                            self._reader.read(TELNET_BUFFER_SIZE),
                            timeout=TELNET_TIMEOUT,
                        )

                        if not data:
                            _LOGGER.warning("Connection closed by server")
                            self._connected = False
                            continue

                        # Process received data
                        await self._process_data(data)

                        # Reset reconnect delay on successful receive
                        self._reconnect_delay = TELNET_RECONNECT_DELAY

                    except asyncio.TimeoutError:
                        # Timeout is normal, just continue
                        continue

            except Exception as err:
                _LOGGER.error("Error in receiver loop: %s", err, exc_info=True)
                self._stats["last_error"] = str(err)
                self._connected = False
                await self._close_connection()

                # Exponential backoff for reconnection
                await asyncio.sleep(self._reconnect_delay)
                self._reconnect_delay = min(
                    self._reconnect_delay * 2,
                    TELNET_MAX_RECONNECT_DELAY,
                )

    async def _connect(self) -> None:
        """Establish telnet connection to the boiler."""
        try:
            _LOGGER.info("Connecting to %s:%d", self._host, self._port)

            self._reader, self._writer = await asyncio.wait_for(
                asyncio.open_connection(self._host, self._port),
                timeout=TELNET_TIMEOUT,
            )

            self._connected = True
            self._stats["reconnections"] += 1
            _LOGGER.info("Connected to boiler")

        except (OSError, asyncio.TimeoutError) as err:
            _LOGGER.error("Failed to connect: %s", err)
            self._stats["last_error"] = f"Connection failed: {err}"
            raise

    async def _close_connection(self) -> None:
        """Close the telnet connection."""
        if self._writer:
            try:
                self._writer.close()
                await self._writer.wait_closed()
            except Exception as err:
                _LOGGER.debug("Error closing connection: %s", err)
            finally:
                self._writer = None
                self._reader = None

        self._connected = False

    async def _process_data(self, data: bytes) -> None:
        """Process received telnet data.

        Args:
            data: Raw bytes received from telnet
        """
        self._stats["messages_received"] += 1

        try:
            # Try multiple encodings
            text = None
            for encoding in ["utf-8", "latin-1", "cp1252"]:
                try:
                    text = data.decode(encoding)
                    break
                except UnicodeDecodeError:
                    continue

            if text is None:
                # Fallback: replace invalid characters
                text = data.decode("utf-8", errors="replace")
                _LOGGER.debug("Used fallback decoding with character replacement")

            # Split into lines and process each
            lines = text.strip().split("\n")

            for line in lines:
                line = line.strip()
                if not line or not line.startswith("pm"):
                    continue

                # Parse message
                try:
                    parsed_data = self._parser.parse_message(line)

                    if parsed_data:
                        # Store data
                        async with self._data_lock:
                            self._latest_data = parsed_data
                            self._last_update = datetime.now()

                        self._stats["messages_parsed"] += 1

                        # Notify callbacks
                        for callback in self._data_callbacks:
                            try:
                                callback(parsed_data)
                            except Exception as err:
                                _LOGGER.error("Error in data callback: %s", err)

                        # Only process the most recent message
                        break

                except Exception as err:
                    _LOGGER.warning("Failed to parse message: %s", err)
                    self._stats["parse_errors"] += 1

        except Exception as err:
            _LOGGER.error("Error processing data: %s", err, exc_info=True)
            self._stats["parse_errors"] += 1

    async def get_latest_data(self) -> dict[str, Any]:
        """Get the latest parsed data.

        Returns:
            Dictionary with latest boiler parameters
        """
        async with self._data_lock:
            return self._latest_data.copy()

    def register_callback(self, callback: Callable[[dict[str, Any]], None]) -> None:
        """Register a callback for new data.

        Args:
            callback: Function to call when new data is available
        """
        if callback not in self._data_callbacks:
            self._data_callbacks.append(callback)

    def unregister_callback(self, callback: Callable[[dict[str, Any]], None]) -> None:
        """Unregister a data callback.

        Args:
            callback: Function to remove from callbacks
        """
        if callback in self._data_callbacks:
            self._data_callbacks.remove(callback)

    @property
    def connected(self) -> bool:
        """Return connection status."""
        return self._connected

    @property
    def last_update(self) -> datetime | None:
        """Return timestamp of last successful update."""
        return self._last_update

    @property
    def statistics(self) -> dict[str, Any]:
        """Return client statistics."""
        return self._stats.copy()

    @property
    def expected_message_length(self) -> int:
        """Return expected message length for current firmware."""
        return self._parser.expected_length
