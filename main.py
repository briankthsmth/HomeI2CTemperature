import signal

from pyhap.accessory_driver import AccessoryDriver
from I2CTemperatureAccessory import I2CTemperatureAccessory
from Display import Display

display = Display()

driver = AccessoryDriver(port=51826)

def handle_change(value):
    if driver.state.paired:
        display.display_temperature(value)

accessory = I2CTemperatureAccessory(handle_change, driver, 'Temperature')
driver.add_accessory(accessory=accessory)

if not driver.state.paired:
    display.draw_qrcode(accessory.xhm_uri(), driver.state.pincode.decode())

signal.signal(signal.SIGTERM, driver.signal_handler)

driver.start()
