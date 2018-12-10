import physense_emu
from time import sleep

sensor = physense_emu.Sensor()


def get_code():
    code = []
    i = 0
    while i < 4:
        if sensor.input('Button_1') == 'pressed':
            code.append('1')
            i += 1
        elif sensor.input('Button_2') == 'pressed':
            code.append('2')
            i += 1
        elif sensor.input('Button_3') == 'pressed':
            code.append('3')
            i += 1
        elif sensor.input('Button_4') == 'pressed':
            code.append('4')
            i += 1
        else:
            sleep(.1)

    return code


def main():
    lock_code = get_code()
    print('lock code =', lock_code)

    unlock_code = get_code()
    print('unlock code =', unlock_code)

    if lock_code == unlock_code:
        print('Unlocked')
    else:
        print('Unlock Failed')


main()
