import logging

from homeassistant.components.fan import (
    FanEntity,
    FanEntityFeature,
)
from homeassistant.components.fan import FanEntity
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity 

from .const import DOMAIN
from .coordinator import BrinkHraModbusCoordinator
from .base_entity import get_device_info

_LOGGER = logging.getLogger(__name__)

PRESETS = {
    "holiday": 0,
    "low": 1,
    "medium": 2,
    "high": 3,
}

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([AirFlow(coordinator, entry.entry_id)])
 
class AirFlow(CoordinatorEntity,FanEntity):
    """Air Flow Fan Entity"""
    _coordinator: BrinkHraModbusCoordinator

    _attr_name = "Air Flow Fan"
    _attr_supported_features = (
        FanEntityFeature.SET_SPEED 
        | FanEntityFeature.PRESET_MODE 
        | FanEntityFeature.TURN_ON 
        | FanEntityFeature.TURN_OFF
    )
    _attr_speed_count = 3  # low/medium/high
    _attr_is_on = False
    _attr_percentage = 0
    _attr_switch_position = 0
    _attr_preset_modes = list(PRESETS.keys())
    _attr_preset_mode = PRESETS["holiday"]

    def __init__(self, coordinator, entry_id):
        super().__init__(coordinator)
        self._entry_id = entry_id
        self._unique_device_id = entry_id  # Required for device_info
        self._attr_unique_id = f"{entry_id}_fan"  # Required for entity registry
        self._coordinator = coordinator
    
    async def async_turn_on(self, percentage=None, preset_mode=None,**kwargs):
        if preset_mode is not None:
            await self.async_set_preset_mode(preset_mode)
        elif percentage is not None:
            await self.async_set_percentage(percentage)
        else:
            await self._coordinator.set_fan_flow_rate(self._coordinator.last_fan_rate)

    async def async_turn_off(self, **kwargs):
        await self._coordinator.set_fan_flow_rate(0)
        await self._coordinator.async_request_refresh()

    async def async_set_percentage(self, percentage):
        if percentage == 0:
            position = 0
        elif percentage <= 33:
            position = 1
        elif percentage <= 66:
            position = 2
        else:
            position = 3

        await self._coordinator.set_fan_flow_rate(position)
        await self._coordinator.async_request_refresh()

    async def async_set_preset_mode(self, preset_mode: str):
        if preset_mode not in PRESETS:
            raise ValueError(f"Invalid preset mode: {preset_mode}")

        await self._coordinator.set_fan_flow_rate(PRESETS[preset_mode])
        await self._coordinator.async_request_refresh()
        
    @property
    def is_on(self):
        return self._coordinator.fan_state > 0

    @property
    def percentage(self):
        return {0: 0, 1: 33, 2: 66, 3: 100}.get(self._coordinator.fan_state, 0)
    
    @property
    def speed_count(self) -> int:
        """Return the number of speeds the fan supports."""
        return self._attr_speed_count

    @property
    def preset_modes(self):
        """Return the list of available preset modes."""
        return self._attr_preset_modes
    
    @property
    def preset_mode(self):
        for name, position in PRESETS.items():
            if position == self._coordinator.fan_state:
                return name
        return "holiday"
    
    @property
    def device_info(self) -> DeviceInfo:
        return get_device_info(self)

   
