import sqlite3
import os

# Четене на данните от файла data.txt
with open('data.txt', 'r') as file:
    data = file.read()

# Парсиране на данните
rows = [line.split('^') for line in data.split('\n')]

# Създаване на нова SQLite база данни
db_name = 'usda_nutrients.db'
if os.path.exists(db_name):
    os.remove(db_name)

conn = sqlite3.connect(db_name)
c = conn.cursor()

# Създаване на таблица
c.execute('''
CREATE TABLE nutrients (
    Retn_Code TEXT,
    Desc TEXT,
    Nutr_No TEXT,
    NutrDesc TEXT,
    Retn_Factor REAL
)
''')

# Попълване на таблицата с данните от файла
for row in rows:
    c.execute('''
    INSERT INTO nutrients (Retn_Code, Desc, Nutr_No, NutrDesc, Retn_Factor)
    VALUES (?, ?, ?, ?, ?)
    ''', [field.strip('~') for field in row[:5]])

conn.commit()

# Извеждане на всички храни, които съдържат 'VEAL'
c.execute("SELECT * FROM nutrients WHERE Desc LIKE '%VEAL%'")
results = c.fetchall()

for result in results:
    print(result)

conn.close()
