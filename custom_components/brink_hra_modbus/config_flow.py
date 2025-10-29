"""Config flow for the Brink HRA Modbus integration."""

import voluptuous as vol
from homeassistant.config_entries import ConfigFlow
from homeassistant.core import callback
from .const import DOMAIN, CONF_HOST, CONF_PORT, DEFAULT_PORT

class BrinkHraModbusConfigFlow(ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input:
            return self.async_create_entry(title="Brink HRA Modbus", data=user_input)

        schema = vol.Schema({
            vol.Required(CONF_HOST): str,
            vol.Optional(CONF_PORT, default=DEFAULT_PORT): int
        })

        return self.async_show_form(step_id="user", data_schema=schema)
