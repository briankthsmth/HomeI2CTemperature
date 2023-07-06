# HomeI2CTemperature

This project uses the [HAP-python](https://github.com/ikalchev/HAP-python) package 
to implement a HomeKit compatable temperature accessory.

## Hardware
- Raspberry Pi Zero W
- [Sparkfun Digital Temperature Sensor Breakout - TMP102](https://www.sparkfun.com/products/13314)

The following table shows the 40 pin header values for wiring the TMP102 breakout board.

| Pin Number | Function |
| --- | --- |
| 1 | 3.3 V |
| 3 | GPIO 2 (SDA) |
| 5 | GPIO 3 (SCL) |
| 6 | Ground |

## I2C Setup

Use `raspi-config` to enable the I2C buses.

Install the following packages:

`sudo apt install i2c-tools python3-smbus`

The default I2C address for the TMP102 chip is 0x48. Once the breakout board is connected, 
it can be verified with the following command.

`i2cdetect -y 1`

If you don't see it the printed table, there is a second I2C bus on PI Zero W which you 
check, otherwise, check your wiring.

## HAP Setup

I've been needing to install [rust](https://www.rust-lang.org/) lately even though
it is not listed as a dependency.

The following are needed to instal the HAP-python package. 

```
sudo apt install libavahi-compat-libdnssd-dev
pip3 install HAP-python[QRCode]
```

On the Zero W, I find this takes a long enough time to build such that a ssh session will 
time out. So, it is best to run this on the device by connecting a keyboard and monitor to it.

## Test It

Run the _main.py_ for the first time to get the QR code or setup code to add the accessory
to the Home app.

## Setup Service

Included in the git repo is a configuration file for running the accessory code 
as a systemd service. The code should be ran initially from the command line in order
to add it to the Home app. After that, it can be ran as a service. The _home-accessory.service_
file assumes the the login user is __pi__, so you will probably need to edit the file to change
the user and working directory before setting up the service.

The following is the command that will setup the service:

```
sudo cp home-accessory.service /etc/systemd/system
sudo systemctl daemon-reload 
sudo systemctl enable home-accessory.service
sudo systemctl start home-accessory.service
sudo systemctl status home-accessory.service
```