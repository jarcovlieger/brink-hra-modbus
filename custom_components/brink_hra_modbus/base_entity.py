from homeassistant.helpers.entity import DeviceInfo
from .const import DOMAIN, DEFAULT_NAME

def get_device_info(self) -> DeviceInfo:
    return DeviceInfo(
        identifiers={(DOMAIN, self._unique_device_id)},
        name=DEFAULT_NAME,
        manufacturer="Brink",
        model="Flair Series",
    )
