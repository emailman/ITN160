import physense_emu
import time

# create sensor
sensor = physense_emu.Sensor()

# flags for alarm snooze and alarm enabled
alarm_enabled = False
snooze_enabled = False


def alarm_check():
    global alarm_enabled
    if sensor.input('Button_3') == 'pressed':
        # toggle the flag
        alarm_enabled = not alarm_enabled

    # set green LED based on the flag
    if alarm_enabled:
        sensor.output('gled', 'on')
    else:
        sensor.output('gled', 'off')


def snooze_check():
    global snooze_enabled
    if sensor.input('Button_4') == 'pressed':
        # toggle the flag
        snooze_enabled = not snooze_enabled

    # set blue LED based on the flag
    if snooze_enabled:
        sensor.output('bled', 'on')
    else:
        sensor.output('bled', 'off')


def print_time():
    current_time = time.localtime(time.time())
    print(time.strftime("%H:%M:%S %p", current_time))


def snooze():
    global snooze_enabled

    # check if the snooze is enabled
    if snooze_enabled:
        # shut the alarm off for 10 seconds
        for i in range(10):
            print_time()
            time.sleep(1)

        # disable the snooze
        snooze_enabled = False


def alarm():
    # turn on the red LED and alarm if light is on,
    # alarm is enabled and the snooze is disabled
    if sensor.input("light") == "on" \
            and alarm_enabled and not snooze_enabled:
        sensor.output('rled', 'on')
        sensor.output("buzz", "play")
    else:
        sensor.output('rled', 'off')


def main():
    while True:
        alarm_check()
        snooze_check()
        print_time()
        alarm()
        snooze()
        time.sleep(1)


main()
