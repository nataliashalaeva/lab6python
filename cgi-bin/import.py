import sqlite3
import xml.etree.ElementTree as ET
import os

print("Content-type: text/html\n")

conn = sqlite3.connect('architecture.db')
cursor = conn.cursor()

current_directory = os.getcwd()
file_path = os.path.join(current_directory, "building.xml")

try:
    tree = ET.parse(file_path)
    root = tree.getroot()

    for building in root.findall('building'):
        name = building.find('name').text
        address = building.find('address').text
        year_built = building.find('year_built').text
        architect = building.find('architect').text

        cursor.execute("INSERT INTO Buildings (name, address, year_built, architect) VALUES (?, ?, ?, ?)",
                       (name, address, year_built, architect))

    conn.commit()
    print("<p>Данные успешно импортированы в базу данных.</p>")
except Exception as e:
    print('<script>alert("Ошибка при импорте данных из XML: {}");</script>'.format(str(e)))

conn.close()

print('<meta http-equiv="refresh" content="0; url=/index.html">')
