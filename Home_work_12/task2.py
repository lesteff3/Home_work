# Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
# переопределить магические методы сравнения(==, !=, >=, <=, <, >
class MyTime:

    def __init__(self, *args):
        if len(args) == 3:
            self.hours, self.minutes, self.seconds = args
        else:
            self.hours, self.minutes, self.seconds = 00, 00, 00
        min = 60
        sec = 60
        hours = 24




        for i in args:

            if self.minutes > 59:
                self.minutes -= min
                self.hours += 1
            elif self.seconds > 59:
                self.seconds -= sec
                self.minutes += 1
            elif self.seconds > 59:
                self.seconds -= sec
                self.seconds = (str(self.seconds).zfill(2))
            elif self.hours > 23:
                self.hours -= hours
                self.hours = (str(self.hours).zfill(2))
            elif self.hours == 24:
                self.hours = (str(self.hours).zfill(2))


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
    my_time = MyTime(23, 80, 70)
    print(my_time)



