import sqlite3
import contextlib
from configuration import *


def sql_insert(data_list_products, section):
    """
    :param data_list_products: get list of dictionaries of all the info for each product.
           Every item in the list is for different product.
    :param section: the chosen section (dresses\tops\swimwear)
    The function insert the info of the products into the database.
    """

    with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
        with con:
            cur = con.cursor()

            for dict in data_list_products:
                cur.execute(f"INSERT OR IGNORE INTO products (Web_ID, Product_type, Price, Average_rating, \
                Reviews_amount, Small, True_to_Size, Large, Style, Color, Pattern_Type, Neckline, Composition, \
                Material, Fabric, Details, Date_exchange_rate, Price_ILS) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            [dict[val] if val in dict else UNKNOWN for val in PRODUCT_COL_LIST])
                con.commit()

                # adding more fields related to t-shirts and dresses to more_desc table:
                cur.execute("INSERT OR IGNORE INTO common_desc (Item_ID, Type, Season, Sleeve_Length, Sleeve_Type,\
                 Sheer, Fit_Type) VALUES (?,?,?,?,?,?,?)",
                            [dict[val] if val in dict else UNKNOWN for val in MORE_DESC_COL_LIST])
                con.commit()

            if section == 'DRESSES':
                for dict in data_list_products:
                    cur.execute("INSERT OR IGNORE INTO dresses (Item_ID, Dresses_Length, Waist_Line, Hem_Shaped, \
                    Belt, Sleeve_Type) VALUES (?,?,?,?,?,?)",
                                [dict[val] if val in dict else UNKNOWN for val in DRESSES_COL_LIST])
                    con.commit()

            elif section == 'TOPS':
                for dict in data_list_products:
                    cur.execute("INSERT OR IGNORE INTO t_shirts (Item_ID, Length, Placket_Type, Arabian_Clothing) \
                    VALUES (?,?,?,?)", [dict[val] if val in dict else UNKNOWN for val in TSHIRTS_COL_LIST])
                    con.commit()

            elif section == 'SWIMWEAR':
                for dict in data_list_products:
                    cur.execute("INSERT OR IGNORE INTO swimwear (Item_ID, Bra, Bottom_Type, Lining, Chest_pad) \
                    VALUES (?,?,?,?,?)", [dict[val] if val in dict else UNKNOWN for val in SWIMWEAR_COL_LIST])
                    con.commit()
