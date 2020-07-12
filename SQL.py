import sqlite3
import os
import contextlib


DB_FILENAME = 'shein.db'
data_list_products = []
data_list_dresses = []
data_list_tshirts = []
data_list_swimwear = []
QUESTION_MARK = "?,"
LEN_LIST_SQL = 0
LEN_PRODUCTS_MINUS1 = 8
LEN_DRESSES_MINUS1 = 20
LEN_TSHIRTS_MINUS1 = 18
LEN_SWIMWEAR_MINUS1 = 13

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


        for line in range(len(data_list_products)):
            if line % 100 == 0:
                print(f"uplaoded {line} lines of table products")
            cur.execute(f"INSERT INTO products VALUES ({LEN_PRODUCTS_MINUS1*QUESTION_MARK}, ?)", data_list_products[line])

        for line in range(len(data_list_dresses)):
            if line % 100 == 0:
                print(f"uplaoded {line} lines of table dresses")
            cur.execute(f"INSERT INTO dresses VALUES ({LEN_DRESSES_MINUS1*QUESTION_MARK}, ?)", data_list_dresses[line])

        for line in range(len(data_list_tshirts)):
            if line % 100 == 0:
                print(f"uplaoded {line} lines of table dresses")
            cur.execute(f"INSERT INTO dresses VALUES ({LEN_TSHIRTS_MINUS1*QUESTION_MARK}, ?)", data_list_tshirts[line])

        for line in range(len(data_list_swimwear)):
            if line % 100 == 0:
                print(f"uplaoded {line} lines of table dresses")
            cur.execute(f"INSERT INTO dresses VALUES ({LEN_SWIMWEAR_MINUS1*QUESTION_MARK}, ?)", data_list_swimwear[line])

