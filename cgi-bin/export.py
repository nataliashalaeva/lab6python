import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('architecture.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM Buildings")
rows = cursor.fetchall()

root = ET.Element("building")

for row in rows:
    building = ET.SubElement(root, "building")

    building_id = ET.SubElement(building, "id")
    building_id.text = str(row[0])

    name = ET.SubElement(building, "name")
    name.text = str(row[1])

    address = ET.SubElement(building, "address")
    address.text = str(row[2])

    year_built = ET.SubElement(building, "year_built")
    year_built.text = str(row[3])

    architect = ET.SubElement(building, "architect")
    architect.text = str(row[4])

tree = ET.ElementTree(root)
tree.write("building.xml", encoding="utf-8")

conn.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/index.html">')
