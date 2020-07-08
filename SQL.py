import sqlite3
import os
import contextlib
from tqdm import tqdm_notebook

DB_FILENAME = 'shein.db'
data_list_products = []
data_list_dresses = []
# if os.path.exists(DB_FILENAME):
#     os.remove(DB_FILENAME)

with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
    with con:  # auto-commits
        cur = con.cursor()
        cur.execute("""CREATE TABLE products(
                    Index INTEGER PK,
                    Web_ID TEXT PK,
                    Type_name TEXT,
                    Price INTEGER,
                    Avg_rate REAL,
                    Reviews_amount INTEGER,
                    Small INTEGER,
                    True_to_size INTEGER,
                    Large INTEGER)""")

        cur.execute("""CREATE TABLE dresses(
                    Index INTEGER PK,
                    Web_ID TEXT FK,
                    Type_name TEXT,
                    Style TEXT,
                    Color TEXT,
                    Pattern_Type TEXT,
                    FOREIGN KEY (Web_ID) REFERENCES products(Web_ID))""")

        for line in range(len(data_list_products)):
            if line % 10000 == 0:
                print(f"uplaoded {line} lines of table products")
            cur.execute("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data_list_products[line])

        for line in range(len(data_list_dresses)):
            if line % 10000 == 0:
                print(f"uplaoded {line} lines of table dresses")
            cur.execute("INSERT INTO dresses VALUES (?, ?, ?, ?, ?)", data_list_dresses[line])

