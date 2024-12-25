import sqlite3


def initiate_db():
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
        )
        ''')

    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
                       (i, f'Product{i}', f'description{i}', i * 100))
    connection.commit()
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()
    cursor.execute('SELECT  * FROM Users WHERE username = ?', (username,))
    result = True if cursor.fetchall() else False
    connection.close()
    return result


def get_all_products():
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products ")
    result = cursor.fetchall()
    connection.close()
    return result


if __name__ == '__main__':
    initiate_db()
