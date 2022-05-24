from contextlib import contextmanager


@contextmanager
def open_file(file_name, mode: str):
    try:
        print('hello from enter!')
        file = open(file_name, mode=mode)
        yield file
    finally:
        if file:
            print('hello from exit!')
            file.close()



if __name__ == "__main__":
    with open_file('new_file.txt', 'w') as new_file:
        new_file.write('str')
        from time import sleep
        sleep(5)