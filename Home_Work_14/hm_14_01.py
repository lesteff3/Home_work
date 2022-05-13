import time
import logging


def countdown(*, name, second_name, hours, minut, num_of_secs):
    while num_of_secs:
        logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        logging.warning(f'{name} {second_name}')
        h, m, s = (hours, minut, num_of_secs)
        hours_min_sec_format = '{:02d}:{:02d}:{:02d}'.format(h, m, s)
        print(hours_min_sec_format, end='\n')
        time.sleep(1)
        num_of_secs -= 1

    print('ALARM!!!')




countdown(name='Maksim', second_name='Kulchinsky', hours=0, minut=0, num_of_secs=3)