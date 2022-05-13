from os.path import abspath, dirname

file_path = abspath(__file__)
file_dir = dirname(file_path)
print(file_path)
print(file_dir)
