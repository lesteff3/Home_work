# Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
# умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
# скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
# разворот(изменение знака скорости). Все атрибуты приватные.


class Car:
    def __init__(self, brand, model, year, speed: int = 0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    def change_speed_5(self):
        self.__speed += 5
        return print(f'Вы выехали на прямую дорогу. Ваша текущая скорость - {self.__speed}')

    def change_speed_minus_5(self):
        self.__speed -= 5
        return print(f'На пути была яма вам пришлось снизить скорость. Ваша текущая скорость - {self.__speed}')

    def change_speed_0(self):
        self.__speed = 0
        return print(f'Вы остановились, ваша скорость - {self.__speed}')

    def get_speed(self):
        return print(f'Ваша скорость - {self.__speed}')

    def reversal(self):
        self.__speed = 10
        return print(f'Разворот, снижение скорости до {self.__speed}!')

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year


car = Car(brand='BMW', model='X5', year=2001)
print(car.brand, car.model, car.year)
car.get_speed()
car.change_speed_5()
car.change_speed_5()
car.change_speed_5()
car.change_speed_5()
car.reversal()
car.change_speed_minus_5()
car.change_speed_0()


