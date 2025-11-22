"""Data update coordinator for Hargassner Pellet Boiler."""
from __future__ import annotations

import logging
from datetime import timedelta
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, UPDATE_INTERVAL
from .src.telnet_client import HargassnerTelnetClient
from .types import ParameterData

_LOGGER = logging.getLogger(__name__)


class HargassnerDataUpdateCoordinator(DataUpdateCoordinator[dict[str, ParameterData]]):
    """Class to manage fetching Hargassner data from telnet client."""

    def __init__(
        self,
        hass: HomeAssistant,
        telnet_client: HargassnerTelnetClient,
        entry: ConfigEntry,
    ) -> None:
        """Initialize the coordinator.

        Args:
            hass: Home Assistant instance
            telnet_client: Telnet client instance
            entry: Config entry
        """
        self.telnet_client = telnet_client
        self.entry = entry

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=UPDATE_INTERVAL),
        )

    async def _async_update_data(self) -> dict[str, ParameterData]:
        """Fetch data from telnet client.

        Returns:
            Dictionary with latest boiler data

        Raises:
            UpdateFailed: If no data available or connection lost
        """
        # Get latest data from telnet client
        data = await self.telnet_client.get_latest_data()

        if not data:
            # Check if connected
            if not self.telnet_client.connected:
                raise UpdateFailed("Not connected to boiler")

            # No data yet, but connected - this is OK on startup
            _LOGGER.debug("No data available yet, but connected")
            return {}

        # Add connection metadata
        data["_connection"] = {
            "connected": self.telnet_client.connected,
            "last_update": self.telnet_client.last_update,
            "statistics": self.telnet_client.statistics,
        }

        return data
