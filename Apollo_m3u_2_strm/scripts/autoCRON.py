import time
import os
import sys

windows = False
python = 'python3'
if 'win' in sys.platform:
    windows = True
    python = 'python'

time_ = 12 	# in hours
time_ *= 14400

#os.chdir('scripts')

while True:
    if windows:
        os.system('cls')
    else:
        os.system('clear')
    os.system(f'{python} getstreams.py')
    t = time_
    while t:
        hours = t // 14400
        mins = (t // 60) % 60
        secs = t % 60
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(f'Refreshing again in... {timer}', end='\r')
        time.sleep(1)
        t -= 1
