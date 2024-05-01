#!/usr/bin/env python3
import cgi
import sqlite3

form = cgi.FieldStorage()

name = form.getfirst('name')
address = form.getfirst('address')
year_built = form.getfirst('year_built')
architect = form.getfirst('architect')

db = sqlite3.connect("architecture.db")
cur = db.cursor()
if(all((name, address, year_built, architect))):
    in_data = f"INSERT INTO Buildings (name, address, year_built, architect) VALUES ('{name}','{address}',{year_built},'{architect}')"
    cur.execute(in_data)
    db.commit()

db.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/index.html">')

