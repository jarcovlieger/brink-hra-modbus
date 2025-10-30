import logging

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from datetime import timedelta
from .brink import Brink

_LOGGER = logging.getLogger(__name__)

class BrinkHrvModbusCoordinator(DataUpdateCoordinator):
    _brink: Brink

    def __init__(self, hass):
        super().__init__(
            hass,
            _LOGGER,
            name="Brink HRV Modbus Coordinator",
            update_interval=timedelta(seconds=5),
        )
       
        self.temperature = None
        self.fan_state = 0
        self.last_fan_rate = 1

    @classmethod
    async def initialize(cls, hass, host, port):
        self = cls(hass)
        self._brink = await Brink.initialize(host, port, 20)
        return self
    
    async def _async_update_data(self):
        try:
            self.temperature = await self._brink.get_supply_fan_temperature()
            self.fan_state = await self._brink.get_switch_position()
        except Exception as e:
            _LOGGER.error("Modbus read failed: %s", e)

    async def set_fan_flow_rate(self, rate: int):
        try:
            await self._brink.set_switch_position(rate)

            if rate > 0:
                self.last_fan_rate = rate
        except Exception as e:
            _LOGGER.error("Modbus write failed: %s", e)