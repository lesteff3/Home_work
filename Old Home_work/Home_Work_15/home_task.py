import sqlite3
from logger import get_logger

logger = get_logger()

'CRUD - Create Read Update Delete'



class Person:

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = self.__get_connection()
        self.cursor = self.__get_cursor()
        self.__creat_table()



    def __get_connection(self):
        try:
            connection = sqlite3.connect(self.db_name)
            logger.debug(f'Connection to db {self.db_name} successfully created!')
            return connection
        except sqlite3.Error as e:
            logger.warning(str(e))
            return e


    def __get_cursor(self):
        return self.connection.cursor()


    def __creat_table(self):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS person(
                person_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name VARCHAR,
                last_name VARCHAR,
                age INTEGER
                )
            """
        self.cursor.execute(create_table_query)


    def get_commit(self):
        self.connection.commit()
        self.connection.close()



    def create_person(self, firstname: str, lastname: str, age: int) -> int:
        CREATE = """INSERT INTO person(first_name, last_name, age) VALUES (?, ?, ?)"""
        self.cursor.execute(CREATE, (firstname, lastname, age))
        self.connection.commit()
        logger.info(f'Person {firstname} {lastname} successfully created!')
        return self.cursor.lastrowid



    def read(self):
        read = self.connection.cursor()
        SELECT_USER_NAME_QUARE = "SELECT * FROM person"
        read.execute(SELECT_USER_NAME_QUARE)
        reading = read.fetchall()
        logger.info(f'Database was reading!')
        for row in reading:
            print(row)



    def delete_person(self, person_id: int):
        DELETE_USER_DATA_QUARE = "DELETE FROM person WHERE person_id=?;"
        self.cursor.execute(DELETE_USER_DATA_QUARE, (person_id,))
        self.connection.commit()
        logger.info(f'Person with {person_id} successfully delete!')



    def uppdate(self, uppdate_firstname: str, firstname: str):
        UPPDATE_USER_DATA_QUARE = "UPDATE person SET first_name= ? WHERE first_name= ?;"
        self.cursor.execute(UPPDATE_USER_DATA_QUARE, (uppdate_firstname, firstname))
        self.connection.commit()
        logger.info(f'Person with {firstname} successfully uppdate on {uppdate_firstname}!')



    def yanger_25(self):
        yang = self.connection.cursor()
        SELECT_AGE_YANGER_25 = "SELECT * FROM person WHERE age < 25;"
        yang.execute(SELECT_AGE_YANGER_25)
        age = yang.fetchall()
        logger.info(f'Person under 25!')
        for row in age:
            print(row)


    def age_more_15_to_18(self):
        age = self.connection.cursor()
        SELECT_AGE_MORE_15_TO_18 = "SELECT * FROM person WHERE age = 15 or age < 18  "
        age.execute(SELECT_AGE_MORE_15_TO_18)
        age_person = age.fetchall()
        logger.info(f'Person over 15 but under 18!')
        for row in age_person:
            print(row)





if __name__ == '__main__':
    person = Person(db_name='database.db')
    # person_id = person.create_person(firstname='Maksim', lastname='Kulchinsky', age=20)
    # person.create_person(firstname='Gleb', lastname='Skotnikov', age=20)
    # person.create_person(firstname='Slava', lastname='Kulchinsky', age=27)
    # person.create_person(firstname='Djo', lastname='Bansen', age=15)
    # person.create_person(firstname='Polina', lastname='Rezontova', age=20)
    # person.delete_person(person_id=1)
    # person.uppdate(uppdate_firstname='Max', firstname='Maksim')

    person.read()