import sqlite3
import contextlib
from configuration import *

with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
    with con:
        cur = con.cursor()
        cur.execute("select * from products")
        for i in cur.fetchall():
            print(i)
