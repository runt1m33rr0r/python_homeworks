import sqlite3
import os
import sys


input = sys.argv[1:]
user_query = input[0]

lines = []

with open('retn5_dat.txt') as f:
    lines = f.readlines()

records = [line.rstrip().split('^') for line in lines]

for idx, line in enumerate(records):
    records[idx] = [word.strip('~') for word in line]

db_file_path = os.path.join(os.path.dirname(__file__), './f87134-food.db')
if os.path.isfile(db_file_path):
    os.remove(db_file_path)

conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

query = """CREATE TABLE food (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT,
    descript TEXT,
    nmbr INTEGER,
    nutname TEXT,
    retention INTEGER
)
"""

cursor.execute(query)

for line in records:
    code, descript, nmbr, nutname, retention = line[0], line[1], line[2], line[3], line[4]

    if not nmbr:
        nmbr = 0
    else:
        nmbr = int(nmbr)

    if not retention:
        retention = 0
    else:
        retention = int(retention)

    query = 'INSERT INTO food(code, descript, nmbr, nutname, retention) VALUES(?, ?, ?, ?, ?)'
    cursor.execute(query, (code, descript, nmbr, nutname, retention))

conn.commit()

cursor.execute(user_query)
result = cursor.fetchone()
print result

conn.close()