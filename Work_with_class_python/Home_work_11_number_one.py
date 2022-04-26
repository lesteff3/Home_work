# Создать три класса: Dog, Cat, Parrot. Атрибуты каждого
# класса: name, age, master. Каждый класс содержит
# конструктор и методы: run, jump, birthday(увеличивает age
# на 1), sleep. Класс Parrot имеет дополнительный метод fly.
# Cat - meow, Dog - bark.


class Dog:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master


    def bark(self):
        print(f'{self.name} Woof!')

    def run(self):
        print(f'{self.name} Run!')

    def jump(self):
        print(f'{self.name} Jump!')

    def birthday(self):
        self.age += 1
        print(f'Ура, день рождения!!! ты стал на год старше, теперь тебе {self.age}')

    def sleep(self):
        print(f'{self.name} sleep')



dog = Dog(name='Bonny', age=1, master='Polina')
dog.run()
dog.jump()
dog.bark()
dog.birthday()


class Cat:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master


    def meow(self):
        print(f'{self.name} Meow!')

    def run(self):
        print(f'{self.name} Run!')

    def jump(self):
        print(f'{self.name} Jump!')

    def birthday(self):
        self.age += 1
        print(f'Ура, день рождения!!! ты стал на год старше, теперь тебе {self.age}')

    def sleep(self):
        print(f'{self.name} sleep')


cat = Cat(name='Margo', age=7, master='Maksim')
cat.meow()
cat.run()
cat.jump()
cat.birthday()
cat.sleep()


class Parrot:


    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def fly(self):
        print(f'{self.name} Flying!')

    def run(self):
        print(f'{self.name} Run!')

    def jump(self):
        print(f'{self.name} Jump!')

    def birthday(self):
        self.age += 1
        print(f'Ура, день рождения!!! ты стал на год старше, теперь тебе {self.age}')

    def sleep(self):
        print(f'{self.name} sleep')


parrot = Parrot(name='Roma', age=14, master='Slava')
parrot.run()
parrot.jump()
parrot.fly()
parrot.birthday()
parrot.sleep()

