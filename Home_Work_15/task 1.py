import sqlite3

CREATE_TABLE_QUARY = """CREATE TABLE user(
                    id integer PRIMARY KEY AUTOINCREMENT,
                    first_name varchar,
                    last_name varchar
            )
"""

CREATE_CAR_TABLE_QUARY = """
                CREATE TABLE IF NOT EXISTS car(
                id integer PRIMARY KEY AUTOINCREMENT,
                    first_name varchar
                    
                )
"""

INSERT_USER_DATA_QUARY = "INSERT INTO user(first_name, last_name) VALUES (?, ?)"
SELECT_USER_DATA_QUARY = "SELECT * FROM user;"


if __name__ == '__main__':
    connection = sqlite3.connect('cw_15.db')
    cursor = connection.cursor()

    cursor.execute(CREATE_CAR_TABLE_QUARY)
    cursor.close()

    connection.commit()

    connection.close()