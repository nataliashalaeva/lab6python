import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect('architecture.db')

# Создание курсора для выполнения SQL-запросов
cur = conn.cursor()

# Создание таблицы для зданий
cur.execute('''CREATE TABLE IF NOT EXISTS Buildings (
                building_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT,
                year_built INTEGER,
                architect TEXT
                )''')

# Создание таблицы для архитекторов
cur.execute('''CREATE TABLE IF NOT EXISTS Architects (
                architect_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                nationality TEXT,
                birth_year INTEGER
                )''')

# Создание таблицы для стилей архитектуры
cur.execute('''CREATE TABLE IF NOT EXISTS ArchitecturalStyles (
                style_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT
                )''')

# Создание таблицы для связи между зданиями и архитекторами (многие ко многим)
cur.execute('''CREATE TABLE IF NOT EXISTS BuildingArchitects (
                building_id INTEGER,
                architect_id INTEGER,
                FOREIGN KEY (building_id) REFERENCES Buildings (building_id),
                FOREIGN KEY (architect_id) REFERENCES Architects (architect_id),
                PRIMARY KEY (building_id, architect_id)
                )''')

# Создание таблицы для связи между зданиями и стилями архитектуры (многие ко многим)
cur.execute('''CREATE TABLE IF NOT EXISTS BuildingStyles (
                building_id INTEGER,
                style_id INTEGER,
                FOREIGN KEY (building_id) REFERENCES Buildings (building_id),
                FOREIGN KEY (style_id) REFERENCES ArchitecturalStyles (style_id),
                PRIMARY KEY (building_id, style_id)
                )''')

cur.execute("DELETE FROM Buildings")


# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
