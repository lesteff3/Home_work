from time import sleep
import logging


def pomodoro(*, name, second_name, hours: int = 0, num_of_secs: int = 0, focus: int = 25, time_break: int = 5,
             repeat: int = 4, task_name):
    logging.basicConfig(filename='logging_name.csv', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.warning(f'{name} {second_name}')
    print('Focus 25 min')
    while focus:
        h, focus, second = (hours, focus, num_of_secs)
        hours_min_sec_format = '{:02d}:{:02d}:{:02d}'.format(h, focus, second)
        print(hours_min_sec_format, end='\n')
        sleep(1)
        focus -= 1

    print('Time Break! 5 min')
    while time_break:
        h, time_break, second = (hours, time_break, num_of_secs)
        hours_min_sec_format = '{:02d}:{:02d}:{:02d}'.format(h, time_break, second)
        print(hours_min_sec_format, end='\n')
        sleep(1)
        time_break -= 1

        repeat -= 1


if __name__ == '__main__':
    pomodoro(name='Maksim', second_name='Kulchinsky', task_name='Pomodoro')
