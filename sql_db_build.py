"""
This file creates the database, and you run it only once.
"""

import sqlite3
import os
import contextlib
from configuration import *

if os.path.exists(DB_FILENAME):
    os.remove(DB_FILENAME)

with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
    with con:
        cur = con.cursor()
        cur.execute(SQL_TABLE_PRODUCTS)
        cur.execute(SQL_TABLE_DRESSES)
        cur.execute(SQL_TABLE_T_SHIRTS)
        cur.execute(SQL_TABLE_SWIMWEAR)
        # common in t-shirts and dresses
        cur.execute(SQL_TABLE_COMMON_DESC)
