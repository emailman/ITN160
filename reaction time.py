import physense_emu
from time import sleep, clock
from random import randint

print('''
Press Button_1 when ready.
When the blue LED comes on, press Button_1 again as quickly as possible.
If your reaction time is good, the green LED will come on for 2 seconds,
otherwise, the red LED will come on for 2 seconds.''')

sensor = physense_emu.Sensor()

start = 0.0
end = 0.0

while True:
    if sensor.input('Button_1') == 'pressed':
        delay = randint(2, 4)
        print('delay =', delay)
        sleep(delay)
        sensor.output('bled', 'on')
        print('ready')
        start = clock()
        break
    else:
        sleep(.1)

while True:
    if sensor.input('Button_1') == 'pressed':
        end = clock()
        react_time = end - start
        print('Done in', react_time)
        sensor.output('bled', 'off')

        if react_time > 2:
            sensor.output('rled', 'on')
            sleep(2)
            sensor.output('rled', 'off')
        else:
            sensor.output('gled', 'on')
            sleep(2)
            sensor.output('gled', 'off')

        break
    else:
        sleep(.1)
