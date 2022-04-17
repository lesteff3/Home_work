# Тренировка с функцией lambda
from datetime import datetime
from functools import reduce

# Задание 9.01
func_name = lambda a: f'Hello, {a}'
print(func_name(input('Input your name : ')))





# # Задание 9.02
name = ['max', 'gleb', 'polina']
new_name = []
for names in name:
    new_name.append(lambda names=names: print(f'"Hello, {names}"'))
for x in new_name:
    x()




# Задание 9.04

some_list_name = ["max", "kostya", "anton", "slava", "karl"]
filter_list = (filter(lambda x: 'k' in x, some_list_name))
print(list(filter_list))




# Задание 9.05
numbers = [2, 3, 6, 10, 11]
print(reduce(lambda x, y: x * y, filter(lambda x: not x % 3, numbers)))





# Задание 9.06

def some_decorator(func):
    def wrapp():
        star_time = datetime.now()
        print(f'Время старта функции {star_time}')
        func()
        end_time = datetime.now()
        print(f'Время окончания функции {end_time}')
        print("Время выполнениния данной функции = ", format(end_time-star_time))
    return wrapp


@some_decorator
def func_sum():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число : '))
    x = a + b
    print(f'{a} + {b} = {x}')


func_sum()