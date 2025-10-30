from pymodbus.client import AsyncModbusTcpClient

class Brink():
    _client: AsyncModbusTcpClient = None 
    _device_id = 20

    def __init__(self, device_id = 20):
        self._device_id = device_id

    @classmethod
    async def initialize(cls, host, port, device_id):
        """Async factory method to return an initialized instance."""
        self = cls(device_id)
        self._client = AsyncModbusTcpClient(host, port=port)
        await self._client.connect()
        return self

    def get_software_version(self) -> str:
        """
        Gets software version.
        :return: version in byte range[0..9].
        """
        major = self.get_major_software_version_number()
        minor = self.get_minor_software_version_number()
        return f"{major}.{minor}"   
    
    def get_minor_software_version_number(self) -> str:
        """
        Gets Type and major version number.
        :return: major nr in byte range[0..9].
        """
        registers = self._client.read_input_registers(address=4001, count=1, device_id=self._device_id)
        byte_array = registers.registers[0].to_bytes(4, byteorder="big")
        number = int(byte_array[1].hex())
        return f"{number}"
    
    def get_major_software_version_number(self) -> str:
        """
        Gets Type and major version number.
        :return: major nr in byte range[0..9].
        """
        registers = self._client.read_input_registers(address=4000, count=1, device_id=self._device_id)
        byte_array = registers.registers[0].to_bytes(4, byteorder="big")
        type_str = byte_array[:3].decode("ascii")
        number = int(byte_array[3:].hex())
        return f"{type_str}{number}"
    
    async def get_supply_fan_temperature(self) -> 'float':
        """
        Gets the supply fan temperature.
        :return: Temperature in degrees Celsius.
        """
        result = await self._client.read_input_registers(address=4036, count=1, device_id=self._device_id)
        return result.registers[0]/10.0 
    
    async def set_modbus_control_switched_on(self, value: int) -> None:
        """
        Sets the Modbus control switched on register.
        :param value: 0 = Off, 1 = switch, 2 = flow rate value
        """
        return await self._client.write_register(address=8000, value=value, device_id=self._device_id)
     
    async def get_modbus_control_switched_on(self) -> None:
        """
        Gets the Modbus control switched on register.
        :return: 0 = Off, 1 = switch, 2 = flow rate value
        """
        result = await self._client.read_holding_registers(address=8000, device_id=self._device_id)
        return result.registers[0]
    
    
    async def set_switch_position(self, value: int) -> None:
        """
        Sets the switch position register.
        :param value: 0 = Holiday, 1 = Low, 2 = Medium, 3 = High
        """
        return await self._client.write_register(address=8001, value=value, device_id=self._device_id)

    async def get_switch_position(self) -> int:
        """
        Gets the switch position register.
        :return: 0 = Holiday, 1 = Low, 2 = Medium, 3 = High
        """
        result = await self._client.read_holding_registers(address=8001, device_id=self._device_id)
        return result.registers[0]

    
