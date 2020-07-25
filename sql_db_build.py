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
        cur.execute("""CREATE TABLE products(
                    Web_ID TEXT PK,
                    Product_type TEXT,
                    Price INTEGER,
                    Average_rating REAL,
                    Reviews_amount INTEGER,
                    Small INTEGER,
                    True_to_Size INTEGER,
                    Large INTEGER,
                    Style TEXT,
	                Color TEXT,
	                Pattern_Type TEXT,
	                Neckline TEXT,
                    Composition TEXT,
                    Material TEXT,
                    Fabric TEXT,
                    Price_ILS REAL,
                    Date_exchange_rate TEXT,
                    UNIQUE (Web_ID) ON CONFLICT IGNORE)""")
        cur.execute('CREATE INDEX i on products(Web_ID)')

        cur.execute("""CREATE TABLE dresses(
                    Web_ID TEXT PK,
                    Dresses_Length TEXT,
                    Type TEXT,
                    Details TEXT,
                    Sleeve_Length TEXT,
                    Season TEXT,
                    Waist_Line TEXT,
                    Sheer TEXT,
                    Hem_Shaped TEXT,
                    Fit_Type TEXT,
                    Belt TEXT,
                    Sleeve_Type TEXT,
                    Lining TEXT,    
                    FOREIGN KEY (Web_ID) REFERENCES products(Web_ID),
                    UNIQUE (Web_ID) ON CONFLICT IGNORE)""")

        cur.execute("""CREATE TABLE t_shirts(
                    Web_ID TEXT PK,
                    Length TEXT,
                    Type TEXT,
                    Details TEXT,
                    Season TEXT,
                    Sheer TEXT,
                    Fit_Type TEXT,
                    Sleeve_Length TEXT,
                    Sleeve_Type TEXT,
                    Placket_Type TEXT,
                    Arabian_Clothing TEXT,
                    FOREIGN KEY (Web_ID) REFERENCES products(Web_ID),
                    UNIQUE (Web_ID) ON CONFLICT IGNORE)""")

        cur.execute("""CREATE TABLE swimwear(
                    Web_ID TEXT PK,
                    Bra TEXT,
                    Type TEXT,
                    Bottom_Type TEXT,
                    Lining TEXT,
                    Chest_pad TEXT,
                    FOREIGN KEY (Web_ID) REFERENCES products(Web_ID),
                    UNIQUE (Web_ID) ON CONFLICT IGNORE)""")

# common in t-shirts and dresses
# Type TEXT,
# Details TEXT,
# Season TEXT,
# Sleeve_Length TEXT,
# Sheer TEXT,
# Fit_Type TEXT,
# Sleeve_Type TEXT,

#we need to adjust them in sql_insert_product, configuration (product_col_list etc)