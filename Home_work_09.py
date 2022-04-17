# Задание 01

string = ['max', 'back', 'go', 'vent']
x = enumerate(string, 1)
print(list(x))



# Задание 02
double_dict_keys = lambda **kwargs: {f'{key}{key}': value for key, value in kwargs.items()}
print(double_dict_keys(a=1))





# Задание 03

def numbers_decorator(func):
    def wrapp():
        print('Производим зачистку четных элементов списка !')
        func()
        print('Сделано!')
    return wrapp



@numbers_decorator
def func_filters():
    a = [10, 20, 22, 1, 3, 5, 7]
    print(a)
    x = list(filter(lambda x: int(x) % 2, a))
    print(x)


func_filters()




# Задание 04

def change_decorator(func):
    def wrapp():
        print('Меняем аргументы местами')
        func()
        print('Готово!')

    return wrapp




@change_decorator
def replacement_args(**kwargs):
    kwargs = {"kwargs_1": "Shark", "kwargs_2": "Max"}
    print(f"Изначальный список аргументов {kwargs}")
    x = dict(zip(kwargs.values(), kwargs.keys()))
    print(f"После изменения {x}")


replacement_args()


