import sqlite3


# Создание подключения к базе данных (или подключение к уже существующей базе данных)
conn = sqlite3.connect('massage_salon.db')
cursor = conn.cursor()

# Создание таблицы для администраторов
def auto_insert():
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Admins VALUES(0, 'admin', 'admin', 'admin')''')
    cursor.execute('''INSERT INTO Employees VALUES(1, 'Alex', 'qwerty', 'employee', 'massager', 90000)''')
    cursor.execute('''INSERT INTO Service VALUES(1, 'standart', 2499)''')
    cursor.execute('''INSERT INTO Service VALUES(2, 'premium', 5499)''')
    cursor.execute('''INSERT INTO Service VALUES(3, 'deluxe', 9999)''')
    conn.commit()
    conn.close()

def create_admin_table():
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Admins (
                             admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
                             username TEXT NOT NULL,
                             password TEXT NOT NULL,
                             status TEXT
                         )''')
    conn.commit()
    conn.close()



# Создание таблицы для продавцов
def create_basket():
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Basket (
                        request_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user TEXT NOT NULL,
                        type TEXT NOT NULL,
                        price INTEGER NOT NULL
                    )''')
    conn.commit()
    conn.close()

# Создание таблицы для услуг
def create_service():
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Service (
                        service_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        type TEXT NOT NULL,
                        price INTEGER NOT NULL
                    )''')
    conn.commit()
    conn.close()

def add_service(id, type, price):
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()

    cursor.execute(f'''INSERT INTO Service VALUES({id}, '{type}', {price})''')

    conn.commit()
    conn.close()

def view_services():
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()
    data = []

    cursor.execute(f"SELECT * FROM Service")
    names = cursor.fetchall()
    for name in names:
        arr = []
        for row in name:
            arr.append(row)
        data.append(arr)

    return data
    conn.commit()
    conn.close()

def delete_service(name):
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()

    cursor.execute(f"""DELETE FROM Service WHERE type = '{name}' """)

    conn.commit()
    conn.close()

# Создание таблицы для сотрудников
def create_employees():
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
                        employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        password TEXT,
                        status TEXT,
                        position TEXT NOT NULL,
                        salary REAL
                    )''')
    conn.commit()
    conn.close()


# Создание таблицы для посетителей
def create_visitors():
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Visitors (
                        visitor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL,
                        status TEXT,
                        phone_number TEXT NOT NULL,
                        email TEXT
                    )''')
    conn.commit()
    conn.close()



def add_data(visitor_id, name, password, status, phone_number, email, ):
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()
    params = (visitor_id, name, password, status, phone_number, email)
    cursor.execute('''INSERT INTO Visitors VALUES(?, ?, ?, ?, ?, ?)''', params)
    conn.commit()
    conn.close()

def clear_data():
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM Visitors''')

    conn.commit()
    conn.close()
def get_all_users():
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()

    data = []
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    names = cursor.fetchall()
    if names != []:
        names.remove(('sqlite_sequence',))
        names.remove(('Service',))
        names.remove(('Basket',))
        for table in names:
            cursor.execute(f'SELECT * FROM {str(table[0])}')
            res = cursor.fetchall()
            for row in res:
                user_data = []
                for i in row:
                    user_data.append(i)
                data.append(user_data)

    return data
    conn.commit()
    conn.close()

def block_user(username):
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()

    cursor.execute(f"""DELETE FROM Visitors WHERE username = '{username}' """)

    conn.commit()
    conn.close()

def make_request(id, username, tariff, price):
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()

    params = (id, username, tariff, price)
    cursor.execute('''INSERT INTO Basket VALUES(?, ?, ?, ?)''', params)

    conn.commit()
    conn.close()

def delete_request(id):
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()

    cursor.execute(f"""DELETE FROM Basket WHERE request_id = '{id}' """)

    conn.commit()
    conn.close()

def view_users(value):
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()
    data = []
    if value == "only_users":
        cursor.execute("SELECT * FROM Visitors")
        names = cursor.fetchall()
        for name in names:
            arr = []
            for row in name:
                arr.append(row)
            data.append(arr)

    elif value == "all_users":
        cursor.execute("SELECT * FROM Visitors")
        names = cursor.fetchall()
        for name in names:
            arr = []
            for row in name:
                arr.append(row)
            data.append(arr)

        cursor.execute("SELECT * FROM Admins")
        names = cursor.fetchall()
        for name in names:
            arr = []
            for row in name:
                arr.append(row)
            data.append(arr)


    return data
    conn.commit()
    conn.close()

def users_basket(username):
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()
    data = []

    cursor.execute(f"SELECT * FROM Basket WHERE user = '{username}'")
    names = cursor.fetchall()
    for name in names:
        arr = []
        for row in name:
            arr.append(row)
        data.append(arr)

    return data
    conn.commit()
    conn.close()

def view_basket():
    conn = sqlite3.connect('massage_salon.db')
    cursor = conn.cursor()
    data = []

    cursor.execute(f"SELECT * FROM Basket")
    names = cursor.fetchall()
    for name in names:
        arr = []
        for row in name:
            arr.append(row)
        data.append(arr)

    return data
    conn.commit()
    conn.close()


# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

