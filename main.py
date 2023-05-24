import signal

from pyhap.accessory_driver import AccessoryDriver
from I2CTemperatureAccessory import I2CTemperatureAccessory

driver = AccessoryDriver(port=51826)
driver.add_accessory(accessory=I2CTemperatureAccessory(driver, 'Temperature'))
                     
signal.signal(signal.SIGTERM, driver.signal_handler)

driver.start()
