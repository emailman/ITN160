import physense_emu
import time

sensor = physense_emu.Sensor()


def blinkLED():
    sensor.output("bled", "on")
    time.sleep(.25)
    sensor.output("bled", "off")
    time.sleep(.25)


def main():

    for i in range(4):
        blinkLED()


main()
