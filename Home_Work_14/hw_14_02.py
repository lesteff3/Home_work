from time import sleep
import logging


def pomodoro(*, name, second_name, focus: int = 25, time_break: int = 5,
             repeat: int = 4, task_name):
    logging.basicConfig(filename='sample.py', format='%(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    logging.warning(f'{name} {second_name}')
    while focus:
        sleep(1)
        focus -= 1
        print(focus)



if __name__ == '__main__':
    pomodoro(name='Maksim', second_name='Kulchinsky', task_name='Pomodoro')

