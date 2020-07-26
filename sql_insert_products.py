import sqlite3
import contextlib
from configuration import *


class Sql_insert_products:
    @staticmethod
    def insert_data(cur, con, col_dict, query, col_list):
        """
        :param cur: connection to cursor
        :param con: creating connection to sqlite
        :param col_dict: dict of product
        :param query: sql query
        :param col_list: list of columns names
        This function commit SQL query, and by that inserting data to table.
        """
        cur.execute(query, [col_dict[val] if val in col_dict else UNKNOWN for val in col_list])
        con.commit()

    @staticmethod
    def sql_insert(data_list_products, section):
        """
        :param data_list_products: get list of dictionaries of all the info for each product.
               Every item in the list is for different product.
        :param section: the chosen section (dresses\tops\swimwear)
        The function insert the info of the products into the database, using the insert_data function.
        """

        with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
            with con:
                cur = con.cursor()

                for dict in data_list_products:
                    Sql_insert_products.insert_data(cur, con, dict, SQL_INSERT_TO_PRODUCTS, PRODUCT_COL_LIST)

                    # adding more fields related to t-shirts and dresses to more_desc table:
                    Sql_insert_products.insert_data(cur, con, dict, SQL_INSERT_TO_COMMON_DESC, MORE_DESC_COL_LIST)

                if section == SQL_DRESSES_SEC:
                    for dict in data_list_products:
                        Sql_insert_products.insert_data(cur, con, dict, SQL_INSERT_TO_DRESSES, DRESSES_COL_LIST)

                elif section == SQL_T_SHIRTS_SEC:
                    for dict in data_list_products:
                        Sql_insert_products.insert_data(cur, con, dict, SQL_INSERT_TO_T_SHIRTS, TSHIRTS_COL_LIST)

                elif section == SQL_SWIMWEAR_SEC:
                    for dict in data_list_products:
                        Sql_insert_products.insert_data(cur, con, dict, SQL_INSERT_TO_SWIMWEAR, SWIMWEAR_COL_LIST)
