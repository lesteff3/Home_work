def memoize_func(f):
    my_dict = dict()


    def func(*args):
        print(f'Args write = {args}, my_dict = {my_dict}')
        if args in my_dict:
            print(f'You have already passed such arguments.{my_dict}')
        elif args not in my_dict:
            my_dict[args] = f(*args)
        return my_dict[args]
    return func


@memoize_func
def func(a, b):
    print(f'Remembering your passed arguments ({a}, {b}) in "my_dict"')
    return a + b



if __name__ == '__main__':
    print(func(3, 5), '\n')
    print(func(3, 4), '\n')
    print(func(3, 2), '\n')
    print('-----------')
    print(func(3, 5), '\n')
    print(func(3, 4), '\n')
    print(func(3, 5), '\n')



