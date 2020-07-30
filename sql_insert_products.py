import pymysql.cursors
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
        values = [col_dict[val] if val in col_dict else UNKNOWN for val in col_list]
        values = tuple(values)
        cur.execute(query, values)
        con.commit()

    @staticmethod
    def update_fk(cur, con, query, item_id):
        """
        :param cur: connection to cursor
        :param con: creating connection to sqlite
        :param query: sql query
        :param item_id: item ID of the product in the products table
        This function commit SQL query, and by that updating the FK in the tables by the products table.
        """
        cur.execute(query, item_id)
        con.commit()

    @staticmethod
    def sql_insert(data_list_products, section):
        """
        :param data_list_products: get list of dictionaries of all the info for each product.
               Every item in the list is for different product.
        :param section: the chosen section (dresses\tops\swimwear)
        The function insert the info of the products into the database, using the insert_data function.
        """
        con = pymysql.connect(host=CONNECT_DB_HOST,
                              user=CONNECT_DB_USER,
                              password='123456',
                              db=CONNECT_DB_DB,
                              charset=CONNECT_DB_CHARSET,
                              cursorclass=pymysql.cursors.DictCursor)
        cur = con.cursor()
        with cur:

            for dict in data_list_products:
                Sql_insert_products.insert_data(cur, con, dict, SQL_INSERT_TO_PRODUCTS, PRODUCT_COL_LIST)

            for dict in data_list_products:
                cur.execute(SQL_ITEM_ID_QUERY, dict[GET_WEB_ID])
                item_id = cur.fetchone()[GET_ITEM_ID]

                # adding more fields related to t-shirts and dresses to more_desc table:
                Sql_insert_products.insert_data(cur, con, dict, SQL_INSERT_TO_COMMON_DESC, MORE_DESC_COL_LIST)
                Sql_insert_products.update_fk(cur, con, SQL_UPDATE_FK_COMMON_DESC, item_id)

                if section == SQL_DRESSES_SEC:
                    Sql_insert_products.insert_data(cur, con, dict, SQL_INSERT_TO_DRESSES, DRESSES_COL_LIST)
                    Sql_insert_products.update_fk(cur, con, SQL_UPDATE_FK_DRESSES, item_id)

                elif section == SQL_T_SHIRTS_SEC:
                    Sql_insert_products.insert_data(cur, con, dict, SQL_INSERT_TO_T_SHIRTS, TSHIRTS_COL_LIST)
                    Sql_insert_products.update_fk(cur, con, SQL_UPDATE_FK_T_SHIRTS, item_id)

                elif section == SQL_SWIMWEAR_SEC:
                    Sql_insert_products.insert_data(cur, con, dict, SQL_INSERT_TO_SWIMWEAR, SWIMWEAR_COL_LIST)
                    Sql_insert_products.update_fk(cur, con, SQL_UPDATE_FK_SWIMWEAR, item_id)


