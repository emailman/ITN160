import physense_emu
from time import sleep, clock
from random import randint

print('''
Press Button_1 when ready.
When the blue LED comes on, press Button_1 again as quickly as possible.
If your reaction time is good, the green LED will come on for 2 seconds,
otherwise, the red LED will come on for 2 seconds.
''')

sensor = physense_emu.Sensor()

start = 0.0
end = 0.0
threshold = 1
min_delay = 2
max_delay = 5

while True:
    while True:
        # Wait for button 1 to be pressed
        if sensor.input('Button_1') == 'pressed':
            # Sleep for a random amount of time
            delay = randint(min_delay, max_delay)
            # print('delay =', delay)
            sleep(delay)

            # Clear button 1 if pressed during the delay
            if sensor.input('Button_1') == 'pressed':
                pass

            # Turn on the blue LED and get the start time
            sensor.output('bled', 'on')
            print('\nReady\n')
            start = clock()
            break
        else:
            sleep(.1)

    while True:
        # Wait for button 1 to be pressed again
        if sensor.input('Button_1') == 'pressed':
            # Capture the end time
            end = clock()

            # Calculate the reaction time
            react_time = end - start
            print('Done in {:.2f} seconds'.format(react_time))
            sensor.output('bled', 'off')

            if react_time > threshold:
                # Light red LED if reaction was too slow
                sensor.output('rled', 'on')
                sleep(2)
                sensor.output('rled', 'off')
            else:
                # Light green LED if reaction was OK
                sensor.output('gled', 'on')
                sleep(2)
                sensor.output('gled', 'off')

            break
        else:
            sleep(.1)
