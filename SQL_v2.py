import sqlite3
import os
import contextlib


DB_FILENAME = 'shein.db'
data_list_products = []

#==============================
#product table:
COL_P_WEB_ID = 'ID'
COL_P_PRODUCT_TYPE = 'Produc# values (:first, :second, :third)"t type'
COL_P_PRICE = 'price'
COL_P_AVERAGE_RATING = 'average_rating'
COL_P_REVIEWS_AMOUNT = 'reviews_amount'
COL_P_SMALL = 'Small'
COL_P_TRUE_TO_SIZE = 'True to Size'
COL_P_LARGE = 'Large'
PRODUCT_COL_LIST = [COL_P_WEB_ID, COL_P_PRODUCT_TYPE, COL_P_PRICE, COL_P_AVERAGE_RATING, COL_P_REVIEWS_AMOUNT,
                    COL_P_SMALL, COL_P_TRUE_TO_SIZE, COL_P_LARGE]

#dresses table
COL_D_WEB_ID = 'ID'
COL_D_PRODUCT_TYPE = 'Product type'
COL_D_STYLE = 'Style'
COL_D_COLOR = 'Color'
COL_D_PATTERN_TYPE = 'Pattern Type'
COL_D_NECKLINE = 'Neckline'
COL_D_DRESS_LENGTH = 'Dresses Length'
COL_D_TYPE = 'Type'
COL_D_DETAILS = 'Details'
COL_D_SLEEVE_LENGTH = 'Sleeve Length'
COL_D_SEASON = 'Season'
COL_D_COMPOSITION = 'Composition'
COL_D_MATERIAL = 'Material'
COL_D_FABRIC = 'Fabric'
COL_D_WAIST_LINE = 'Waist Line'
COL_D_SHEER = 'Sheer'
COL_D_HEM_SHAPED = 'Hem Shaped'
COL_D_FIT_TYPE = 'Fit Type'
COL_D_BELT = 'Belt'
COL_D_SLEEVE_TYPE = 'Sleeve Type'
COL_D_LINING = 'Lining'
DRESSES_COL_LIST = [COL_D_WEB_ID, COL_D_PRODUCT_TYPE, COL_D_STYLE, COL_D_COLOR, COL_D_PATTERN_TYPE, COL_D_NECKLINE,
                    COL_D_DRESS_LENGTH, COL_D_TYPE, COL_D_DETAILS, COL_D_SLEEVE_LENGTH, COL_D_SEASON, COL_D_COMPOSITION,
                    COL_D_MATERIAL, COL_D_FABRIC, COL_D_WAIST_LINE, COL_D_SHEER, COL_D_HEM_SHAPED, COL_D_FIT_TYPE,
                    COL_D_BELT, COL_D_SLEEVE_TYPE, COL_D_LINING]

#T-shirts/tops table
COL_T_WEB_ID = 'ID'
COL_T_PRODUCT_TYPE = 'Product type'
COL_T_STYLE = 'Style'
COL_T_COLOR = 'Color'
COL_T_PATTERN_TYPE = 'Pattern Type'
COL_T_NECKLINE = 'Neckline'
COL_T_LENGTH = 'Length'
COL_T_TYPE = 'Type'
COL_T_DETAILS = 'Details'
COL_T_SEASON = 'Season'
COL_T_COMPOSITION = 'Composition'
COL_T_MATERIAL = 'Material'
COL_T_FABRIC = 'Fabric'
COL_T_SHEER = 'Sheer'
COL_T_FIT_TYPE = 'Fit Type'
COL_T_SLEEVE_LENGTH = 'Sleeve Length'
COL_T_SLEEVE_TYPE = 'Sleeve Type'
COL_T_PLACKET_TYPE = 'Placket Type'
COL_T_ARABIAN_CLOTHING = 'Arabian Clothing'
TSHIRTS_COL_LIST = [COL_T_WEB_ID, COL_T_PRODUCT_TYPE, COL_T_STYLE, COL_T_COLOR, COL_T_PATTERN_TYPE, COL_T_NECKLINE,
                    COL_T_LENGTH, COL_T_TYPE, COL_T_DETAILS, COL_T_SEASON, COL_T_COMPOSITION, COL_T_MATERIAL,
                    COL_T_FABRIC, COL_T_SHEER, COL_T_FIT_TYPE, COL_T_SLEEVE_LENGTH, COL_T_SLEEVE_TYPE,
                    COL_T_PLACKET_TYPE, COL_T_ARABIAN_CLOTHING]

#swimwear table
COL_S_WEB_ID = 'ID'
COL_S_PRODUCT_TYPE = 'Product type'
COL_S_STYLE = 'Style'
COL_S_COLOR = 'Color'
COL_S_PATTERN_TYPE = 'Pattern Type'
COL_S_NECKLINE = 'Neckline'
COL_S_DETAILS = 'Details'
COL_S_COMPOSITION = 'Composition'
COL_S_MATERIAL = 'Material'
COL_S_FABRIC = 'Fabric'
COL_S_BRA_TYPE = 'Bra Type'
COL_S_BOTTOM_TYPE = 'Bottom Type'
COL_S_LINING = 'Lining'
COL_S_CHEST_PAD = 'Chest pad'
SWIMWEAR_COL_LIST = [COL_S_WEB_ID, COL_S_PRODUCT_TYPE, COL_S_STYLE, COL_S_COLOR, COL_S_PATTERN_TYPE, COL_S_NECKLINE,
                     COL_S_DETAILS, COL_S_COMPOSITION, COL_S_MATERIAL, COL_S_FABRIC, COL_S_BRA_TYPE, COL_S_BOTTOM_TYPE,
                     COL_S_LINING, COL_S_CHEST_PAD]


def build_col_list(column_list):
    output = ""
    for i in column_list:
        if column_list.index(i) == (len(column_list)-1):
            output += f":'{i}' "
        else:
            output += f":'{i}', "
    return output



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
            cur.execute(f"INSERT INTO products VALUES ({build_col_list(PRODUCT_COL_LIST)})", data_list_products[line])

        for line in range(len(data_list_products)):
            if line % 100 == 0:
                print(f"uplaoded {line} lines of table dresses")
            cur.execute(f"INSERT INTO dresses VALUES ({build_col_list(DRESSES_COL_LIST)})", data_list_products[line])

        for line in range(len(data_list_products)):
            if line % 100 == 0:
                print(f"uplaoded {line} lines of table T-shirts")
            cur.execute(f"INSERT INTO t_shirts VALUES ({build_col_list(TSHIRTS_COL_LIST)})", data_list_products[line])

        for line in range(len(data_list_products)):
            if line % 100 == 0:
                print(f"uplaoded {line} lines of table swimwear")
            cur.execute(f"INSERT INTO swimwear VALUES ({build_col_list(SWIMWEAR_COL_LIST)})", data_list_products[line])

