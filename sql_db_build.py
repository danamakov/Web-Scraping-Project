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
                    Item_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Web_ID TEXT,
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
                    Details TEXT,
                    Price_ILS REAL,
                    Date_exchange_rate TEXT,
                    UNIQUE (Web_ID) ON CONFLICT IGNORE)""")

        cur.execute("""CREATE TABLE dresses(
                    Dress_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Item_ID INTEGER,
                    Dresses_Length TEXT,
                    Waist_Line TEXT,
                    Hem_Shaped TEXT,
                    Belt TEXT,
                    Sleeve_Type TEXT,  
                    FOREIGN KEY (Item_ID) REFERENCES products(Item_ID),
                    UNIQUE (Item_ID) ON CONFLICT IGNORE)""")

        cur.execute("""CREATE TABLE t_shirts(
                    T_Shirt_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Item_ID INTEGER,
                    Length TEXT,
                    Placket_Type TEXT,
                    Arabian_Clothing TEXT,
                    FOREIGN KEY (Item_ID) REFERENCES products(Item_ID),
                    UNIQUE (Item_ID) ON CONFLICT IGNORE)""")

        cur.execute("""CREATE TABLE swimwear(
                    Swimwear_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Item_ID INTEGER,
                    Bra TEXT,
                    Bottom_Type TEXT,
                    Lining TEXT,
                    Chest_pad TEXT,
                    FOREIGN KEY (Item_ID) REFERENCES products(Item_ID),
                    UNIQUE (Item_ID) ON CONFLICT IGNORE)""")

        # common in t-shirts and dresses
        cur.execute("""CREATE TABLE common_desc(
                    Common_Desc_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Item_ID INTEGER,
                    Type TEXT,
                    Season TEXT,
                    Sleeve_Length TEXT,
                    Sleeve_Type TEXT,
                    Sheer TEXT,
                    Fit_Type TEXT,
                    FOREIGN KEY (Item_ID) REFERENCES products(Item_ID),
                    UNIQUE (Item_ID) ON CONFLICT IGNORE)""")
