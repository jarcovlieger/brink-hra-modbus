from .const import DOMAIN
from .binary_sensors.filter_status_binary_sensor import FilterStatusBinarySensor

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = coordinator = hass.data[DOMAIN][entry.entry_id]
    
    async_add_entities([
        FilterStatusBinarySensor(coordinator, entry.entry_id)
    ])


