from string import ascii_letters
from random import choice, randint

class Pet:


    @staticmethod
    def get_random_name():
        random_letter = choice(ascii_letters)
        random_number = randint(0, 99)
        return f'{random_letter}-{random_number}'


if __name__ == '__main__':
    print(Pet.get_random_name())