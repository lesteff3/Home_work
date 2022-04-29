# Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
# переопределить магические методы сравнения(==, !=, >=, <=, <, >
class MyTime:

    def __init__(self, *args):
        if len(args) == 3:
            self.hours, self.minutes, self.seconds = args
        else:
            self.hours, self.minutes, self.seconds = 0, 0, 0

        for i in args:
            if i > 60:
                print('Вы передали не существующее время')


    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    def __int__(self):
        return self.hours, self.minutes, self.seconds


    """__eq__ Определяет поведение оператора равенства, =="""
    def __eq__(self, other):
        return all([
            self.hours == other.hours,
            self.minutes == other.minutes,
            self.seconds == other.seconds,
        ])

    """__ne__ Определяет поведение оператора неравенства, !="""
    def __ne__(self, other):
        return all([
            self.hours != other.hours,
            self.minutes != other.minutes,
            self.seconds != other.seconds,

        ])

    """__ge__ Определяет поведение оператора больше или равно, >=."""
    def __ge__(self, other):
        return all([
            self.hours >= other.hours,
            self.minutes >= other.minutes,
            self.seconds >= other.seconds,

        ])

    """__le__ Определяет поведение оператора меньше или равно, <="""
    def __le__(self, other):
        return all([
            self.hours <= other.hours,
            self.minutes <= other.minutes,
            self.seconds <= other.seconds,

        ])

    """Определяет поведение оператора меньше, <"""
    def __lt__(self, other):
        return all([
            self.hours < other.hours,
            self.minutes < other.minutes,
            self.seconds < other.seconds,

        ])
    """Определяет поведение оператора больше, >"""
    def __gt__(self, other):
        return all([
            self.hours > other.hours,
            self.minutes > other.minutes,
            self.seconds > other.seconds,

        ])

    """Складывает"""
    def __add__(self, other):
        return self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds

    """Отнимает"""
    def __sub__(self, other):
        return self.hours - other.hours, self.minutes - other.minutes, self.seconds - other.seconds

    def __mul__(self, other):
        return self.hours * other.hours, self.minutes * other.minutes, self.seconds * other.seconds





if __name__ == '__main__':
    my_time = MyTime(20, 60, 20)
    my_time2 = MyTime(16, 60, 31)



