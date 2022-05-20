import os
from argparse import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f', '--folder-name', required=True)
    parser.add_argument('-n', '--new-file', required=True)
    args = parser.parse_args()

    file_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(file_path)
    new_file = os.path.dirname(file_path)
    os.mkdir(f'{dir_name}/{args.folder_name}')


