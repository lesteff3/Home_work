import sqlite3

'CRUD - Create Read Update Delete'



class Person:

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = self.get_connection()



    def get_connection(self):
        try:
            return sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            with open('log.txt') as file:
                file.write(str(e))
                return f'ERROR'


    def get_cursore(self):
        cursor = self.connection.cursor()
        CREATE_TABLE_QUARY = """
                        CREATE TABLE user (
                         id integer PRIMARY KEY AUTOINCREMENT,
                         firstname varchar(255),
                         lastname varchar(255),
                         age integer
                        )
        """
        cursor.execute(CREATE_TABLE_QUARY)
        cursor.close()

    def get_commit(self):
        self.connection.commit()
        self.connection.close()



    def create_person(self):
        create = self.connection.cursor()
        CREATE = """INSERT INTO user(firstname, lastname, age) VALUES (?, ?, ?)"""
        create.executemany(CREATE, [
            ('Maksim', 'Kulchinsky', 20),
            ('Djec', 'Bansen', 15),
            ('Polina', 'Rezontova', 19),
            ('Gleb', 'Skotnikov', 12),
            ('Vlad', 'Skameiko', 35)
        ])

    def read(self):
        read = self.connection.cursor()
        SELECT_USER_NAME_QUARE = "SELECT * FROM user"
        read.execute(SELECT_USER_NAME_QUARE)
        reader = read.fetchall()
        for row in reader:
            print(row)

    def delete(self):
        delete_user = self.connection.cursor()
        DELETE_USER_DATA_QUARE = "DELETE FROM user WHERE id = 8;"
        delete_user.execute(DELETE_USER_DATA_QUARE)


    def uppdate(self):
        uppdate_user = self.connection.cursor()
        UPPDATE_USER_DATA_QUARE = "UPDATE user SET firstname='Max' WHERE firstname='Maksim';"
        uppdate_user.execute(UPPDATE_USER_DATA_QUARE)



    def yanger_25(self):
        yang = self.connection.cursor()
        SELECT_AGE_YANGER_25 = "SELECT * FROM user WHERE age < 25;"
        yang.execute(SELECT_AGE_YANGER_25)
        age = yang.fetchall()
        for row in age:
            print(row)


    def age_more_15_to_18(self):
        age = self.connection.cursor()
        SELECT_AGE_MORE_15_TO_18 = "SELECT * FROM user WHERE age = 15 or age < 18  "
        age.execute(SELECT_AGE_MORE_15_TO_18)
        age_person = age.fetchall()
        for row in age_person:
            print(row)





if __name__ == '__main__':
    person = Person(db_name='cw.db')
    person.get_connection()
    person.read()
    person.uppdate()
    print('---------')
    person.read()
    print('-------')
    person.yanger_25()
    print('--------')
    person.age_more_15_to_18()
    person.get_commit()