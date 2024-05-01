import sqlite3
# Подключение к базе данных
conn = sqlite3.connect('architecture.db')
cur = conn.cursor()

# Вставка данных в таблицу зданий
buildings_data = [
    ('Empire State Building', '350 5th Ave, New York, NY 10118, USA', 1931, 'Shreve, Lamb & Harmon'),
    ('Taj Mahal', 'Dharmapuri, Forest Colony, Tajganj, Agra, Uttar Pradesh 282001, India', 1653, 'Ustad Ahmad Lahauri'),
    ('Eiffel Tower', 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France', 1889, 'Gustave Eiffel')
]

cur.executemany("INSERT INTO Buildings (name, address, year_built, architect) VALUES (?, ?, ?, ?)", buildings_data)

# Вставка данных в таблицу архитекторов
architects_data = [
    ('Shreve, Lamb & Harmon', 'American', 1878),
    ('Ustad Ahmad Lahauri', 'Indian', None),
    ('Gustave Eiffel', 'French', 1832)
]

cur.executemany("INSERT INTO Architects (name, nationality, birth_year) VALUES (?, ?, ?)", architects_data)

# Вставка данных в таблицу стилей архитектуры
styles_data = [
    ('Neoclassical', 'Inspired by classical architecture of ancient Greece and Rome.'),
    ('Gothic', 'Characterized by pointed arches, ribbed vaults, and flying buttresses.'),
    ('Baroque', 'Known for its grandeur, dramatic themes, and ornate decoration.'),
    ('Modernism', 'Emphasizes function and simplicity over ornamentation.'),
    ('Art Deco', 'Features geometric shapes, vibrant colors, and decorative motifs.')
]

cur.executemany("INSERT INTO ArchitecturalStyles (name, description) VALUES (?, ?)", styles_data)

# Вставка данных в таблицу связей между зданиями и архитекторами
building_architects_data = [
    (1, 1),  # Empire State Building - Shreve, Lamb & Harmon
    (2, 2),  # Taj Mahal - Ustad Ahmad Lahauri
    (3, 3)   # Eiffel Tower - Gustave Eiffel
]

cur.executemany("INSERT INTO BuildingArchitects (building_id, architect_id) VALUES (?, ?)", building_architects_data)

# Вставка данных в таблицу связей между зданиями и стилями архитектуры
building_styles_data = [
    (1, 4),  # Empire State Building - Modernism
    (2, 1),  # Taj Mahal - Neoclassical
    (3, 5)   # Eiffel Tower - Art Deco
]

cur.executemany("INSERT INTO BuildingStyles (building_id, style_id) VALUES (?, ?)", building_styles_data)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

