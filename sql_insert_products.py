import sqlite3
import contextlib
from configuration import *


def remove_duplicates(table):
    """
    :param table: get the section table name
    :return: delete all duplicate rows from the table
    """
    with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
        with con:
            cur = con.cursor()
            cur.execute(f" CREATE TABLE temp as SELECT DISTINCT * FROM {table}; ")
            cur.execute(f" DELETE FROM {table}; ")
            cur.execute(f" INSERT INTO {table} SELECT * FROM temp; ")
            cur.execute(" DROP TABLE IF EXISTS temp ")


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
                cur.execute("INSERT INTO products VALUES (?,?,?,?,?,?,?,?)",
                            [dict[val] if val in dict else UNKNOWN for val in PRODUCT_COL_LIST])
                con.commit()
            # removing duplicates
            remove_duplicates(SEC_PRODUCTS)

            if section == 'DRESSES':
                for dict in data_list_products:
                    cur.execute("INSERT INTO dresses VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                [dict[val] if val in dict else UNKNOWN for val in DRESSES_COL_LIST])
                    con.commit()
                # removing duplicates
                remove_duplicates(SEC_DRESSES)

            elif section == 'TOPS':
                for dict in data_list_products:
                    cur.execute("INSERT INTO t_shirts VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                [dict[val] if val in dict else UNKNOWN for val in TSHIRTS_COL_LIST])
                    con.commit()
                # removing duplicates
                remove_duplicates(SEC_TOPS)

            elif section == 'SWIMWEAR':
                for dict in data_list_products:
                    cur.execute("INSERT INTO swimwear VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                [dict[val] if val in dict else UNKNOWN for val in SWIMWEAR_COL_LIST])
                    con.commit()
                # removing duplicates
                remove_duplicates(SEC_SWIMWEAR)


