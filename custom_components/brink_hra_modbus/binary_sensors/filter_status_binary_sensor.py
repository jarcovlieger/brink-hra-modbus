from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)

from ..entity import BrinkEntity

class FilterStatusBinarySensor(BrinkEntity, BinarySensorEntity):
    """Binary sensor for the filter status"""
    
    _attr_name = "Filter Status"
    _attr_device_class =  BinarySensorDeviceClass.PROBLEM
    _attr_should_poll = False 
    
    def __init__(self, coordinator, entry_id):
        super().__init__(coordinator, entry_id)
        self._attr_unique_id = f"{entry_id}_filter_status"         

    @property
    def is_on(self):
        """Return True if filter is dirty"""
        return self.coordinator.filter_dirty
