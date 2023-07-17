import signal

from pyhap.accessory_driver import AccessoryDriver
from I2CTemperatureAccessory import I2CTemperatureAccessory
from Display import Display

display = Display()

driver = AccessoryDriver(port=51826)
driver.add_accessory(accessory=I2CTemperatureAccessory(display, driver, 'Temperature'))
                     
signal.signal(signal.SIGTERM, driver.signal_handler)

driver.start()
