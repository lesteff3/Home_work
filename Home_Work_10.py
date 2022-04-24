from typing import List
# Задание 10.01

# Первая и пятая строка
def print_selected_line(file_name: str, line_number: int = 5):
    my_file = open(file_name)
    counter = 0

    while counter != line_number:

        line = my_file.readline()
        if not line:
            print('File size is less than 5')
            break

        if counter +1 == line_number:
            print(line)

        counter += 1

    my_file.close()


print_selected_line('some_file.txt', line_number=1)
print_selected_line('some_file.txt', line_number=5)

# 5 строк
def print_all_line():
    f = open('some_file.txt')
    for line in f:
        print(line)


print_all_line()
# Принтиться 2 строчки файла
def print_two_line():
    x = open('some_file.txt')
    print(x.readline())
    print(x.readline(-1))

    x.close()


print_two_line()

# Принтиться весь файл
def print_some_file():
    file = open('some_file.txt')
    print(file.readlines())

    file.close()


print_some_file()


# Задание 10.02


def write_line(file_name: str):

    with open(file_name, 'w') as my_file:
        for _ in range(6):
            input_string = input('Введите вашу строку: ')
            my_file.write(f'{input_string}\n')

    return True

write_line('some_file.txt')


# Задание 10.03

def write_some_line(file_name: str):
    with open(file_name, 'a') as my_file:
        for _ in range(3):
            a = input('Введите ваше дополнение: ')
            my_file.write(f'{a}\n')

        return True

write_some_line('some_file.txt')


# Задание 10.04

file = open('some_file.txt', 'r')
out = open('new_file.txt', 'w')
while True:
    c = file.read(1)
    if len(c) < 1:
        break
    if c == '1':
        out.write('0')
    elif c == '0':
        out.write('1')
    else:
        out.write(c)
out.close()
file.close()


# Задание 10.05

with open('some_file.txt') as file_one:
    with open('new_file.txt', 'w') as file_two:
        with open('filter_file.txt', 'w') as file_three:
            lines = file_one.readlines()
            file_two.writelines(lines[::2])
            file_three.writelines(lines[1::2])

# Задание 10.06

count = 0
eq = True
with open('some_file.txt', 'r') as f1:
    with open('filter_file.txt', 'r') as f2:
        for a1, a2 in zip(f1,f2):
            count += 1
            if a1 != a2:
                eq = False
                break
print(f'Нет отличий') if eq else print(f'Отличается строка номер {count}')