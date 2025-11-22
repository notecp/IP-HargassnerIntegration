"""The Hargassner Pellet Boiler integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady

from .const import DOMAIN
from .coordinator import HargassnerDataUpdateCoordinator
from .src.telnet_client import HargassnerTelnetClient

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Hargassner Pellet Boiler from a config entry."""
    _LOGGER.info("Setting up Hargassner integration for %s", entry.data.get(CONF_HOST))

    # Create telnet client
    telnet_client = HargassnerTelnetClient(
        host=entry.data[CONF_HOST],
        firmware_version=entry.data.get("firmware", "V14_1HAR_q1"),
    )

    # Create coordinator
    coordinator = HargassnerDataUpdateCoordinator(
        hass=hass,
        telnet_client=telnet_client,
        entry=entry,
    )

    # Start telnet client and wait for initial data
    try:
        await telnet_client.async_start()
        await coordinator.async_config_entry_first_refresh()
    except Exception as err:
        await telnet_client.async_stop()
        raise ConfigEntryNotReady(f"Failed to connect to boiler: {err}") from err

    # Store coordinator
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    # Setup platforms
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    _LOGGER.info("Unloading Hargassner integration")

    # Unload platforms
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        coordinator: HargassnerDataUpdateCoordinator = hass.data[DOMAIN].pop(entry.entry_id)
        await coordinator.telnet_client.async_stop()

    return unload_ok


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)
