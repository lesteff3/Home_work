from typing import List


class Pat:

    __counter = 0

    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
        Pat.__counter += 1

    @classmethod
    def get_counter(cls):
        return cls.__counter

    def fly(self):
        print(f'{self.name} Flying!')


    def run(self):
        pass

    def jump(self, miters: int):
        return print(f'Jump {miters} miters!')

    def change_weight(self, diff: int = 0.2):
        self.weight += diff

    def change_height(self, diff: int = 0.2):
        self.height += diff

    def voice(self):
        pass


class Dog(Pat):

    def jump(self, miters: float):
        if miters > 0.5:
            print(f'{self.name} cannot jump so high!')
        else:
            print(f'Jump {miters} miters!')

    def voice(self):
        print(f'Woof ! I am {self.__class__.__name__.lower() } a {self.name}')



class Cat(Pat):

    def jump(self, miters: float):
        if miters > 2:
            print(f'{self.__name__} cannot jump so high!')
        else:
            print(f'Jump {miters} miters!')


    def voice(self):
        print(f'Meow ! I am {self.__class__.__name__.lower() } a {self.name}')



class Parrot(Pat):

    def __init__(self, species: str, can_speak: bool = False, *args, **kwargs):
        super(Parrot, self).__init__(*args, **kwargs)
        self.can_speak = can_speak
        self.species = species



    def fly(self):
        if self.weight < 0.1:
            print('This parrot cannot fly')
        else:
            print('fly')

    def change_weight(self, diff: int = 0.05):
        self.weight += diff
        print(self.weight)

    def change_height(self, diff: int = 0.05):
        self.height += diff
        print(self.height)

    def jump(self, miters: float):
        if miters > 0.05:
            print('Parrot cannot jump so high!')
        else:
            print(f'Jump {miters} miters!')

    def voice(self):
        print(f'Hello ! I am {self.__class__.__name__.lower() } a {self.name}')


def animal_voice(animals_list: List[Pat]):
    for animal in animals_list:
        animal.voice()



if __name__ == "__main__":
    parrot = Parrot(name='Roma', weight=0.2, height=3, species='Volnisty')
    cat = Cat(name='Margo', weight=1, height=2)
    dog = Dog(name='Ozzy', weight=0.5, height=1)
    animal_voice(animals_list=[cat, dog, parrot])
    print(Cat.get_counter())



