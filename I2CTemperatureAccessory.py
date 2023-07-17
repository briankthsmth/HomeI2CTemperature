import time
import smbus

from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_SENSOR
from Display import Display

class I2CTemperatureAccessory(Accessory):
    category = CATEGORY_SENSOR
    i2c_channel = 1
    i2c_address = 0x48
    register_temp = 0x00

    
    def __init__(self, display, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.display = display
        
        # Setup the I2C bus
        self.i2c_bus = smbus.SMBus(self.i2c_channel)

        # Setup the HAP service for this accessory
        service_temp = self.add_preload_service('TemperatureSensor')
        self.char_temp = service_temp.configure_char('CurrentTemperature')
        self.char_temp.setter_callback = self.handle_temperature_change
        
    @Accessory.run_at_interval(3)
    async def run(self):
        self.char_temp.set_value(self.read_temperature())


    def handle_temperature_change(self, value):
        #self.display.display_temperature(value)
        
    def read_temperature(self):
        value = self.i2c_bus.read_i2c_block_data(self.i2c_address, self.register_temp, 2)

        temperature_c = (value[0] << 4) | (value[1] >> 4)
        temperature_c = self.two_complement(temperature_c, 12)
        # The register number is a integer count of temperature steps, so it needs to be
        # converted by 0.0625 degrees celius per count
        temperature_c = 0.0625 * temperature_c
        
        return temperature_c

    def two_complement(self, value, bits):
        if (value & (1 << (bits - 1))) != 0:
            value = value - (1 << bits)

        return value
