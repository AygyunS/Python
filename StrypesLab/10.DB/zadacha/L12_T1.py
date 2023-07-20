# YourEmail_L12_T1.py
import sqlite3
import os
import sys

if len(sys.argv) != 2:
    print("Usage: python YourEmail_L12_T1.py <query>")
    exit(1)

query = sys.argv[1]

# Четене на данните от файла data.txt
with open('data.txt', 'r') as file:
    data = file.read()

# Парсиране на данните
rows = [line.split('^') for line in data.split('\n')]

# Създаване на нова SQLite база данни
db_name = 'aygyun.salim-food.db'
if os.path.exists(db_name):
    os.remove(db_name)

conn = sqlite3.connect(db_name)
c = conn.cursor()

# Създаване на таблицата food
c.execute('''
CREATE TABLE food (
    code TEXT,
    descript TEXT,
    nmbr TEXT,
    nutname TEXT,
    retention REAL
)
''')

# Попълване на таблицата food с данните от файла
for row in rows:
    c.execute('''
    INSERT INTO food (code, descript, nmbr, nutname, retention)
    VALUES (?, ?, ?, ?, ?)
    ''', [field.strip('~') for field in row[:5]])

conn.commit()

# Извършване на заявката от командния ред
c.execute(query)
result = c.fetchone()

if result:
    print(result)
else:
    print("No results found.")

conn.close()
