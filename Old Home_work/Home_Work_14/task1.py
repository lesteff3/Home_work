from time import sleep
from random import randint


def my_gen(value_from: int, value_to: int, delay: int):
    while True:
        sleep(delay)
        yield randint(value_from, value_to)


if __name__ == '__main__':
    for random_value in my_gen(1, 100, 1):
        print(random_value)