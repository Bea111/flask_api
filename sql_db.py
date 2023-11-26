"""
import sqlite3

conn = sqlite3.connect("people.db")

columns = [
    "id INTEGER PRIMARY KEY",
    "lname VARCHAR UNIQUE",
    "fname VARCHAR",
    "timestamp DATETIME",
]

create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
conn.execute(create_table_cmd)
"""

import sqlite3
from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


ans = get_timestamp()
print(ans)

conn = sqlite3.connect("people.db")

people = [
    "1, 'Fairy', 'Tooth', '2023-11-26 16:42:45'",
    "2, 'Ruprecht', 'Knecht', '2023-11-26 16:42:45'",
    "3, 'Bunny', 'Easter', '2023-11-26 16:42:45'",
]


for person_data in people:
    insert_cmd = f"INSERT INTO person VALUES ({person_data})"
    conn.execute(insert_cmd)

conn.commit()
