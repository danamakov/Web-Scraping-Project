import sqlite3
import contextlib
from configuration import *

table = "products"
with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
    with con:
        cur = con.cursor()
        cur.execute(f"select * from {table}")
        for i in cur.fetchall():
            print(i)
