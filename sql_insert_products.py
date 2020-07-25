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
                cur.execute("INSERT OR IGNORE INTO products VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            [dict[val] if val in dict else UNKNOWN for val in PRODUCT_COL_LIST])
                cur.execute('CREATE INDEX i on products(Web_ID)')
                con.commit()

            if section == 'DRESSES':
                for dict in data_list_products:
                    cur.execute("INSERT OR IGNORE INTO dresses VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                [dict[val] if val in dict else UNKNOWN for val in DRESSES_COL_LIST])
                    con.commit()

            elif section == 'TOPS':
                for dict in data_list_products:
                    cur.execute("INSERT OR IGNORE INTO t_shirts VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                                [dict[val] if val in dict else UNKNOWN for val in TSHIRTS_COL_LIST])
                    con.commit()

            elif section == 'SWIMWEAR':
                for dict in data_list_products:
                    cur.execute("INSERT OR IGNORE INTO swimwear VALUES (?,?,?,?,?,?)",
                                [dict[val] if val in dict else UNKNOWN for val in SWIMWEAR_COL_LIST])
                    con.commit()
