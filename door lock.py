import physense_emu
from time import sleep

"""
This simulates a lock with a four digit code.
The code is entered using four push buttons.
Once entered, the blue led is turned on.
Then, if the user enters the correct code,
the green led is turned on, if not, the
red led is turned on.
When the light is turned off, the program exits. 
"""
sensor = physense_emu.Sensor()


def get_code():
    # Return a list of the 4 digit code entered
    code = []
    i = 0
    while i < 4:
        if sensor.input('Button_1') == 'pressed':
            code.append('1')
            i += 1
            print(i, code)
        elif sensor.input('Button_2') == 'pressed':
            code.append('2')
            i += 1
            print(i, code)
        elif sensor.input('Button_3') == 'pressed':
            code.append('3')
            i += 1
            print(i, code)
        elif sensor.input('Button_4') == 'pressed':
            code.append('4')
            i += 1
            print(i, code)
        else:
            sleep(.1)

    return code


def main():
    # Get the lock code, then turn on the blue led
    lock_code = get_code()
    print('lock code =', lock_code)
    sensor.output('bled', 'on')

    # Loop while waiting for the unlock code
    # to be entered
    while True:
        if sensor.input('light') == 'on':
            unlock_code = get_code()
            print('unlock code =', unlock_code)

            # Compare the lock code to the unlock code
            if lock_code == unlock_code:
                print('Unlocked')
                sensor.output('gled', 'on')
                sleep(2)
                sensor.output('gled', 'off')
            else:
                print('Unlock Failed')
                sensor.output('rled', 'on')
                sleep(2)
                sensor.output('rled', 'off')
        else:
            # If the light is off, exit
            sensor.output('bled', 'off')
            break


main()
