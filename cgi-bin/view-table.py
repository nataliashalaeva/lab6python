import cgi
import sqlite3

print("Content-type: text/html\n")

conn = sqlite3.connect('architecture.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM Buildings")

rows = cursor.fetchall()

print("<!DOCTYPE html>")
print("<html lang='ru'>")
print("<head>")
print(" <meta charset='UTF-8'>")
print("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
print("<title>Содержимое таблицы</title>")
print("</head>")
print("<body>")
print("<h1>Содержимое таблицы</h1>")
print("<table>")
print("<tr><th>ID</th><th>Имя</th><th>Адрес</th><th>Год</th><th>Архитектор</th></tr>")

for row in rows:
    print("<tr>")
    print("<td>{}</td>".format(row[0]))
    print("<td>{}</td>".format(row[1]))
    print("<td>{}</td>".format(row[2]))
    print("<td>{}</td>".format(row[3]))
    print("<td>{}</td>".format(row[4]))
    print("</tr>")

print("</table>")
print("<a href='../index.html'><button>Back</button></a>")  # Ссылка на вашу главную страницу или другую страницу, откуда пришли
print("</body>")
print("</html>")

conn.close()