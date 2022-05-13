import argparse
import csv


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first-name', required=True)
    parser.add_argument('-ln', '--last-name', required=True)
    parser.add_argument('-a', '--age', required=True)
    args = parser.parse_args()

    with open('names.csv', 'a', newline='') as my_file:
        writer = csv.writer(my_file)
        writer.writerow([args.first_name, args.last_name, args.age])


if __name__ == '__main__':
    main()