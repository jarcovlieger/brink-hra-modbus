"""The Brink HRA Modbus integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from .const import DOMAIN, CONF_HOST, CONF_PORT
from .coordinator import BrinkHrvModbusCoordinator

# TODO List the platforms that you want to support.
# For your initial PR, limit it to 1 platform.
_PLATFORMS: list[Platform] = [Platform.SENSOR, Platform.FAN, Platform.BINARY_SENSOR]

# TODO Create ConfigEntry type alias with API object
# Alias name should be prefixed by integration name
type New_NameConfigEntry = ConfigEntry[MyApi]  # noqa: F821


# TODO Update entry annotation
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Brink HRA Modbus from a config entry."""

    host = entry.data[CONF_HOST]
    port = entry.data[CONF_PORT]

    coordinator = await BrinkHrvModbusCoordinator.initialize(hass, host, port)
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator

    await coordinator.async_config_entry_first_refresh()

    await hass.config_entries.async_forward_entry_setups(entry, _PLATFORMS)

    return True


# TODO Update entry annotation
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, _PLATFORMS)
