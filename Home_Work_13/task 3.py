from abc import ABC, abstractmethod


class Pet(ABC):

    def __init__(self, name: str):
        self.name = name


    def __str__(self):
        return self.name

    @abstractmethod
    def get_voice(self):
        pass



class Horse(Pet):

    def get_voice(self):
        return f'igogo {self.name}'


class Donkey(Pet):

    def get_voice(self):
        return f'ia {self.name}'


class Mule(Donkey):
    pass


if __name__ == '__main__':
    horse = Horse(name='horse')
    print(horse.get_voice())
    donkey = Donkey(name='donkey')
    print(donkey.get_voice())
    mule = Mule(name='mule')
    print(mule.get_voice())
