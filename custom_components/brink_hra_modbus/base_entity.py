from homeassistant.helpers.entity import DeviceInfo
from .const import DOMAIN

def get_device_info(self) -> DeviceInfo:
    return DeviceInfo(
        identifiers={(DOMAIN, self._unique_device_id)},
        name="Brink Heat Recovery Appliance",
        manufacturer="Brink",
        model="Flair Series",
    )
