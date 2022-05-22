class FileCM:
    def __init__(self, file_name: str, mode: str):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        print('Hello from enter to file. Opening file')
        self.file = open(self.file_name, mode=self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print('Hello from exit. Close file!')
            self.file.close()


if __name__ == '__main__':
    with FileCM('new_file.txt', 'w') as new_file:
        new_file.write('new_str')