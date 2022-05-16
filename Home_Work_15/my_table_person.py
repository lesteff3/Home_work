import sqlite3

'CRUD - Create Read Update Delete'


# class Person:
#
#     def __init__(self, db_name: str):
#         self.db_name = db_name
#
#
#     def create(self):
#         pass
#
#     def read(self):
#         pass
#
#     def update(self):
#         pass
#
#     def delete(self):
#         pass


CREATE_TABLE_QUARY = """
                CREATE TABLE user (
                 id integer PRIMARY KEY AUTOINCREMENT,
                 firstname varchar(255),
                 lastname varchar(255),
                 age integer
                )
"""

INSERT_USER_DATA_QUARY = "  INSERT INTO user (firstname, lastname, age) VALUES (?, ?, ?)"

DELETE_USER_DATA_QUARE = "DELETE FROM user WHERE id = 1;"

SELECT_USER_NAME_QUARE = "SELECT * FROM user WHERE firstname = 'Maksim';"

SELECT_AGE_YANGER_25 = "SELECT * FROM user WHERE age < 25;"

SELECT_AGE_MORE_15_TO_18 = "SELECT * FROM user WHERE age = 15 or age < 18  "


if __name__ == '__main__':
    sql = Person(db_name='my.db')
    connection = sqlite3.connect('my.db')
    cursor = connection.cursor()

    print('People who has name "Maksim"')
    print('----------')

    cursor.execute(SELECT_USER_NAME_QUARE)
    data = cursor.fetchall()
    for row in data:
        print(row)


    print('-----------------')
    print('People who younger 25 ')

    cursor.execute(SELECT_AGE_YANGER_25)
    age = cursor.fetchall()
    for row in age:
        print(row)

    print('------------')
    print('People whose age is from 15 to 18')

    cursor.execute(SELECT_AGE_MORE_15_TO_18)
    ages = cursor.fetchall()
    for row in ages:
        print(row)


    cursor.close()
    connection.commit()
    connection.close()