"""Platform for sensor integration."""

from __future__ import annotations

import logging

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import (
    UnitOfTemperature
) 
from homeassistant.helpers.update_coordinator import CoordinatorEntity 
from homeassistant.helpers.entity import DeviceInfo
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN
from .base_entity import get_device_info
from .coordinator import BrinkHraModbusCoordinator

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([SupplyFanTemperature(coordinator, entry.entry_id)])

class SupplyFanTemperature(CoordinatorEntity, SensorEntity):
    """Supply Fan Temperature Sensor"""
    _coordinator: BrinkHraModbusCoordinator

    _attr_name = "Supply Fan Temperature"
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_should_poll = False  # do not call update()
   
    def __init__(self, coordinator, entry_id):
        super().__init__(coordinator)
        self._entry_id = entry_id
        self._unique_device_id = entry_id  # Required for device_info
        self._attr_unique_id = f"{entry_id}_supply_fan_temp"  # Required for entity registry
        self._coordinator = coordinator
   
    @property
    def native_value(self):
        return self._coordinator.temperature

    @property
    def device_info(self) -> DeviceInfo:
        return get_device_info(self)