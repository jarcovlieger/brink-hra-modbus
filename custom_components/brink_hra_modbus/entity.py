from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.entity import DeviceInfo
from .const import DOMAIN 

class BrinkEntity(CoordinatorEntity):
    """Base entity for integration."""
    
    _attr_has_entity_name = True
    
    def __init__(self, coordinator, entry_id) -> None:
        """Initialize the entity."""
        super().__init__(coordinator)
        self._entry_id = entry_id
        self._unique_device_id = entry_id
        
    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self._unique_device_id)},
            name="Brink Heat Recovery Appliance",
            manufacturer="Brink",
            model="Flair Series",
    )
