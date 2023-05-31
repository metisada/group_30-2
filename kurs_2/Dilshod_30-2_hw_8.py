import sqlite3

conn = sqlite3.connect('dbname.db')
cursor = conn.cursor()

# Создание таблицы countries
cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
''')

countries_name = [('Кыргызстан',), ('Германия',), ('Китай',)]
cursor.executemany('INSERT INTO countries (title) VALUES (?)', countries_name)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries (id)
    )
''')

cities_data = [('Бишкек', 1230000.45, 1), ('Ош', 670000.89, 1), ('Берлин', 4560000.78, 2), ('Мюнхен', 9870000.65, 2),
('Пкеин', 980000.65, 3), ('Шанхай', 6770000.65, 3), ('Кашгар', 5870000.65, 3)]
cursor.executemany('INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)', cities_data)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities (id)
    )
''')

employees_data = [
    ('Иван', 'Иванов', 1),
    ('Петр', 'Петров', 1),
    ('Алексей', 'Сидоров', 2),
    ('Елена', 'Смирнова', 2),
    ('Анна', 'Кузнецова', 2),
    ('Мария', 'Васильева', 3),
    ('Дмитрий', 'Попов', 3),
    ('Александр', 'Лебедев', 3),
    ('Ксения', 'Новикова', 4),
    ('Андрей', 'Морозов', 4),
    ('Александра', 'Волкова', 4),
    ('Ирина', 'Алексеева', 4),
    ('Ольга', 'Лебедева', 4),
    ('Виктор', 'Соловьев', 4),
    ('Артем', 'Михайлов', 4)
]

cursor.executemany('INSERT INTO employees (first_name, last_name, city_id) VALUES (?, ?, ?)', employees_data)

conn.commit()
conn.close()

conn = sqlite3.connect('dbname.db')
cursor = conn.cursor()

cursor.execute('SELECT title FROM cities')
cities = cursor.fetchall()

print('Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:')
for city in cities:
    print(city[0])

city_id = int(input('Введите id города: '))

if city_id != 0:

    cursor.execute('''
            SELECT employees.first_name, employees.last_name, countries.title, cities.title
            FROM employees
            INNER JOIN cities ON employees.city_id = cities.id
            INNER JOIN countries ON cities.country_id = countries.id
            WHERE cities.id = ?
        ''', (city_id,))
    employees = cursor.fetchall()

if employees:
        print('Имя\tФамилия\tСтрана\t\tГород')
        for employee in employees:
            print(f'{employee[0]}\t{employee[1]}\t{employee[2]}\t{employee[3]}')
else:
        print('В выбранном городе нет сотрудников.')

conn.close()