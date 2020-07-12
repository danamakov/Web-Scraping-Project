import sqlite3
import os
import contextlib
from configuration import *


if os.path.exists(DB_FILENAME):
    os.remove(DB_FILENAME)

with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
    with con:  # auto-commits
        cur = con.cursor()
        cur.execute("""CREATE TABLE products(
                    Web_ID TEXT PK,
                    Product_type TEXT,
                    Price INTEGER,
                    Average_rating REAL,
                    Reviews_amount INTEGER,
                    Small INTEGER,
                    True_to_Size INTEGER,
                    Large INTEGER)""")

        cur.execute("""CREATE TABLE dresses(
                    Web_ID TEXT PK,
                    Product_type TEXT,
                    Style TEXT,
                    Color TEXT,
                    Pattern_Type TEXT,
                    Neckline TEXT,
                    Dresses_Length TEXT,
                    Type TEXT,
                    Details TEXT,
                    Sleeve_Length TEXT,
                    Season TEXT,
                    Composition TEXT,
                    Material TEXT,
                    Fabric TEXT,
                    Waist_Line TEXT,
                    Sheer TEXT,
                    Hem_Shaped TEXT,
                    Fit_Type TEXT,
                    Belt TEXT,
                    Sleeve_Type TEXT,
                    Lining TEXT,    
                    FOREIGN KEY (Web_ID) REFERENCES products(Web_ID))""")

        cur.execute("""CREATE TABLE t_shirts(
                    Web_ID TEXT PK,
                    Product_type TEXT,
                    Style TEXT,
                    Color TEXT,
                    Pattern_Type TEXT,
                    Neckline TEXT,
                    Length TEXT,
                    Type TEXT,
                    Details TEXT,
                    Season TEXT,
                    Composition TEXT,
                    Material TEXT,
                    Fabric TEXT,
                    Sheer TEXT,
                    Fit_Type TEXT,
                    Sleeve_Length TEXT,
                    Sleeve_Type TEXT,
                    Placket_Type TEXT,
                    Arabian_Clothing TEXT,
                    FOREIGN KEY (Web_ID) REFERENCES products(Web_ID))""")

        cur.execute("""CREATE TABLE swimwear(
                    Web_ID TEXT PK,
                    Product_type TEXT,
                    Style TEXT,
                    Color TEXT,
                    Pattern_Type TEXT,
                    Neckline TEXT,
                    Composition TEXT,
                    Material TEXT,
                    Fabric TEXT,
                    Bra TEXT,
                    Type TEXT,
                    Bottom_Type TEXT,
                    Lining TEXT,
                    Chest_pad TEXT,
                    FOREIGN KEY (Web_ID) REFERENCES products(Web_ID))""")