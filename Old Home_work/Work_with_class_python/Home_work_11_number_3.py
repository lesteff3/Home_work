# Создать пять классов описывающие реальные объекты. Каждый класс
# должен содержать минимум три приватных атрибута, конструктор, геттеры
# и сеттеры для каждого атрибута, два метода.

class Wood:


    def __init__(self, name, height, age):
        self.__name = name
        self.__height = height
        self.__age = age


    def summer(self):
        return print(f'Лето! {self.__name} пустила свои плоды')

    def snow(self):
        return print(f'Зима! {self.__name} скинула все листья')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


wood = Wood(name='Apple tree', height=1, age=1)
wood.summer()
wood.snow()
print(wood.name, wood.height, wood.age)
wood.name = 'Plum'
wood.height = 2
wood.age = 2
wood.summer()
print(wood.name, wood.height, wood.age)


class Rodents:

    def __init__(self, name, height, age):
        self.__name = name
        self.__height = height
        self.__age = age


    def run(self):
        return print(f'{self.__name} бежит в своем колесе')

    def water(self):
        return print(f'{self.__name} пьёт воду')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


rodents = Rodents(name='Bonny', height=0.5, age=0.2)
print(rodents.name, rodents.height, rodents.age)
rodents.run()
rodents.water()
rodents.name = 'Gammy'
rodents.height = 1
rodents.age = 2
print(rodents.name, rodents.height, rodents.age)


class Dog:

    def __init__(self, name, age, master):
        self.__name = name
        self.__age = age
        self.__master = master


    def bark(self):
        return print(f'{self.__name} Woof!')

    def run(self):
        return print(f'{self.__name} Run!')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master


dog = Dog(name='Bobick', age=2, master='Maksim')
print(dog.name, dog.age, dog.master)
dog.run()
dog.bark()
dog.master = 'Slava'
print(dog.name, dog.age, dog.master)



class Cat:
    def __init__(self, name, age, master):
        self.__name = name
        self.__age = age
        self.__master = master


    def meow(self):
        print(f'{self.__name} Meow!')

    def run(self):
        print(f'{self.__name} Run!')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master


cat = Cat(name='Margo', age='9', master='Irina')
print(cat.name, cat.age, cat.master)
cat.run()
cat.meow()
cat.master = 'Pavel'
print(cat.name, cat.age, cat.master)


class Parrot:


    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def fly(self):
        print(f'{self.name} Flying!')

    def sleep(self):
        print(f'{self.name} sleep')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master


parrot = Parrot(name='Roma', age=15, master=None)
print(parrot.name, parrot.age, parrot.master)
parrot.master = 'Maksim'
print(parrot.name, parrot.age, parrot.master)
parrot.fly()
parrot.sleep()




