import sqlite3


def initiate_db():
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price TEXT NOT NULL
    )
    ''')
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
                       (i, f'Product{i}', f'description{i}', i * 100))
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products ")
    result = cursor.fetchall()
    connection.close()
    return result
