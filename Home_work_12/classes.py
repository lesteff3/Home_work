import math
from math import pi
from typing import List


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y



    def centre(self):
        a = (self.x + self.y) / 2
        return f'{a}'

    def perimeter(self):
        pass



class Figure:
    pass


class Circle(Point):

    def __init__(self, radius: float, *args, **kwargs):
        super(Circle, self).__init__(*args, **kwargs)
        self.radius = radius

    def perimeter(self):
        perimeter = 2 * pi * self.radius
        print(f'Периметр круга = {perimeter}')


    def square(self):
        area = pi * (self.radius**2)
        print(f'Площадь круга = {area}')


class Triangle(Point):

    def __init__(self, z: float, *args, **kwargs):
        super(Triangle, self).__init__(*args, **kwargs)
        self.z = z


    def square(self):
        p = (self.x + self.y + self.z) / 2
        s = (p * (p - self.x) * (p - self.y) * (p - self.z))**0.5
        print(f'Площадь треугольника = {s}')

    def perimeter(self):
        get_perimeter = self.x + self.y + self.z
        print(f'Периметр треугольника = {get_perimeter}')


class Square(Point):

    def square(self):
        get_square = self.x * self.y
        print(f'Площадь квадрата = {get_square}')


    def perimeter(self):
        get_perimeter = self.x * self.x * self.y * self.y
        print(f'Периметр квадрата = {get_perimeter}')



def figure_perimeter(figure_list: List[Point]):
    for figure in figure_list:
        figure.perimeter()












