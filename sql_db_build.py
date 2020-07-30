"""
This file creates the database, and you run it only once.
"""

import pymysql.cursors
import mysql.connector
from configuration import *

# Create database
con = mysql.connector.connect(host=CONNECT_DB_HOST,
                              user=CONNECT_DB_USER,
                              password='1234')

cur = con.cursor()
cur.execute(SQL_CREATE_DB)

# Create tables
con = pymysql.connect(host=CONNECT_DB_HOST,
                      user=CONNECT_DB_USER,
                      password='1234',
                      db=CONNECT_DB_DB,
                      charset=CONNECT_DB_CHARSET,
                      cursorclass=pymysql.cursors.DictCursor)

cur = con.cursor()
with cur:
    cur = con.cursor()
    cur.execute(SQL_TABLE_PRODUCTS)
    cur.execute(SQL_TABLE_DRESSES)
    cur.execute(SQL_TABLE_T_SHIRTS)
    cur.execute(SQL_TABLE_SWIMWEAR)
    cur.execute(SQL_TABLE_COMMON_DESC)
