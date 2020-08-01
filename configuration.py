"""
A file with all const variables.
In order to change their value it must be changed in this file
"""

# main_scrap constants:
PRODUCT_SCRAP_OPT = {'t', 'a', 'd', 's', 'T', 'A', 'D', 'S'}
SCRAP_LIMIT = 1000
COLOR_SCRAP_OPT = ['Blue', 'Pink', 'Green', 'Red', 'Multi', 'Purple', 'Brown', 'White',
                       'Grey', 'Yellow', 'Khaki', 'Black', 'Orange']
SECTION_DICT = {'t': 'TOPS', 'd': 'DRESSES', 's': 'SWIMWEAR'}
LOGGING_NEW_RUN = "----------- << NEW RUN {} >> -----------"


# exchange_api constants:
API_REQUEST = 'https://api.ratesapi.io/api/{}?base={}&symbols={}'
BASE_EX_RATE = 'USD' #from which coin do the exchange
SYMBOL_EX_RATE = 'ILS' #to which coin do the exchange
GET_RATE_JASON_EX = 'rates'
GET_DATE_JASON_EX = 'date'


# shein constants:
URL = "https://us.shein.com/"
NUMBER_OF_PAGES = 2  # The maximum number of pages in the website, you can change this number to lower number.
COLORS_LIST = ['Blue', 'Pink', 'Green', 'Red', 'Multi', 'Purple', 'Brown', 'White', 'Grey', 'Yellow', 'Khaki', 'Black', 'Orange']
LOW_PRICE = 0
HTML_PRS = 'html.parser'
URL_PAGE_FIND_TYPE = 'a'
URL_PAGE_TITLE = "title"
PRODUCT_URL_PAGE_SPLIT = '"'
PRODUCT_URL_PAGE_SPLIT_NUM = 3
PROD_COLOR_SPAN = "span"
PROD_COLOR_CLASS = "class"
PROD_COLOR_CLASS_NAME = "attr-item-pic j-attr-item"
PROD_COLOR_SPLIT_SIGN = '>'
HREF = 'href="'
STRIP_SIGN = '"'
LOOP_COLOR_NUM = 0
URL_CHOICE_PRICE = '?currency=USD&min_price={}&max_price={}'


# product_info constants:
PAGE = "&page={}"
URL_FIND_TYPE = 'a'
URL_SPLIT_SIGN ='href='
TEMP_SPLIT_NUM = 1
URL_PROD_SPLIT_NUM = 1
URL_PROD_SPLIT_SIGN = '"'
HTML_END = ".html"
FROM = 1
TO = -4
LOGGING_FORMAT = '%(asctime)s %(message)s'
LOGGING_FILE_NAME = 'logging.log'
LOGGING_FILE_MODE = 'a'
LOGGING_ATT_ERROR = 'There is a problem with the url: {}'
LOGGING_VAL_ERROR = 'There is a problem with the url: {}'


# data_product constants:
DIV = 'div'
CLASS = 'class'
SPAN = 'span'
ID = "ID"
CLASS_ID = "product-intro__head-sku"
ID_SPLIT_NUM = 1
PRICE = "price"
PRICE_EXCHANGE ='Price_ILS'
DATE_EXCHANGE ='Date_exchange_rate'
CLASS_PRICE = "product-intro__head-price"
PRICE_SPLIT_NUM = 1
PRICE_SPLIT_SIGN = "$"
RATE = "average_rating"
CLASS_RATE = "ave-rate"
RVW_AMOUNT = "reviews_amount"
CLASS_RVW_AMOUNT = "product-intro__head-reviews-text color-blue-text"
RVW_AMNT_SPLIT_NUM = 0
CLASS_FIT = "fit-item"
FIT_FIRST_SPLIT_NUM = 0
FIT_SEC_SPLIT_NUM = 1
FIT_SPLIT_TYPE = "  "
CLASS_DESCRIPTION = "product-intro__description-table-item"
DESC_FIRST_SPLIT_NUM = 0
DESC_SEC_SPLIT_NUM = 1
DESC_SPLIT_TYPE = ":"
ROUND_PRICE_EX = 2
PRODUCT_TYPE = 'Product_type'


# html_soup constants:
HEADLESS = "--headless"
CHROME_DRIVER = "chromedriver"
TIME_SLEEP = 2
HTML_PARSER = 'html.parser'

# sql_insert constants:
DB_FILENAME = 'shein_db.db'
UNKNOWN = 'UNKNOWN'
SEC_PRODUCTS = 'products'
SEC_DRESSES = 'dresses'
SEC_TOPS = 't_shirts'
SEC_SWIMWEAR = 'swimwear'

## product table:
COL_P_WEB_ID = 'ID'
COL_P_PRODUCT_TYPE = 'Product_type'     # values (:first, :second, :third)"t type'
COL_P_PRICE = 'price'
COL_P_AVERAGE_RATING = 'average_rating'
COL_P_REVIEWS_AMOUNT = 'reviews_amount'
COL_P_SMALL = 'Small'
COL_P_TRUE_TO_SIZE = 'True to Size'
COL_P_LARGE = 'Large'
COL_P_STYLE = 'Style'
COL_P_COLOR = 'Color'
COL_P_PATTERN_TYPE = 'Pattern Type'
COL_P_NECKLINE = 'Neckline'
COL_P_COMPOSITION = 'Composition'
COL_P_MATERIAL = 'Material'
COL_P_FABRIC = 'Fabric'
COL_P_DETAILS = 'Details'
COL_P_DATE_EXCHANGE = 'Date_exchange_rate'
COL_P_PRICE_EXCHANGE = 'Price_ILS'
PRODUCT_COL_LIST = [COL_P_WEB_ID, COL_P_PRODUCT_TYPE, COL_P_PRICE, COL_P_AVERAGE_RATING, COL_P_REVIEWS_AMOUNT,
                    COL_P_SMALL, COL_P_TRUE_TO_SIZE, COL_P_LARGE, COL_P_STYLE, COL_P_COLOR, COL_P_PATTERN_TYPE,
                    COL_P_NECKLINE, COL_P_COMPOSITION, COL_P_MATERIAL, COL_P_FABRIC, COL_P_DETAILS,
                    COL_P_DATE_EXCHANGE, COL_P_PRICE_EXCHANGE]


## dresses table
COL_D_WEB_ID = 'ID'
COL_D_DRESS_LENGTH = 'Dresses Length'
COL_D_WAIST_LINE = 'Waist Line'
COL_D_HEM_SHAPED = 'Hem Shaped'
COL_D_BELT = 'Belt'
COL_D_LINING = 'Lining'
DRESSES_COL_LIST = [COL_D_DRESS_LENGTH, COL_D_WAIST_LINE, COL_D_HEM_SHAPED, COL_D_BELT]

## T-shirts/tops table
COL_T_WEB_ID = 'ID'
COL_T_LENGTH = 'Length'
COL_T_PLACKET_TYPE = 'Placket Type'
COL_T_ARABIAN_CLOTHING = 'Arabian Clothing'
TSHIRTS_COL_LIST = [COL_T_LENGTH, COL_T_PLACKET_TYPE, COL_T_ARABIAN_CLOTHING]

## swimwear table
COL_S_WEB_ID = 'ID'
COL_S_BRA_TYPE = 'Bra Type'
COL_S_BOTTOM_TYPE = 'Bottom Type'
COL_S_LINING = 'Lining'
COL_S_CHEST_PAD = 'Chest pad'
SWIMWEAR_COL_LIST = [COL_S_BRA_TYPE, COL_S_BOTTOM_TYPE, COL_S_LINING, COL_S_CHEST_PAD]

## more_desc table
COL_M_WEB_ID = 'ID'
COL_M_TYPE = 'Type'
COL_M_SEASON = 'Season'
COL_M_SLEEVE_LENGTH = 'Sleeve Length'
COL_M_SLEEVE_TYPE = 'Sleeve Type'
COL_M_SHEER = 'Sheer'
COL_M_FIT_TYPE = 'Fit Type'

MORE_DESC_COL_LIST = [COL_M_TYPE, COL_M_SEASON, COL_M_SLEEVE_LENGTH, COL_M_SLEEVE_TYPE,
                      COL_M_SHEER, COL_M_FIT_TYPE]

# sql queries of sql_insert_products file
CONNECT_DB_HOST = 'localhost'
CONNECT_DB_USER = 'root'
CONNECT_DB_PASSWORD = 'Ab123456'
CONNECT_DB_DB = 'shein'
CONNECT_DB_CHARSET = 'utf8mb4'

SQL_INSERT_TO_PRODUCTS = """INSERT IGNORE INTO products (Web_ID, Product_type, Price, Average_rating, 
                        Reviews_amount, Small, True_to_Size, Large, Style, Color, Pattern_Type, Neckline, Composition,
                        Material, Fabric, Details, Date_exchange_rate, Price_ILS) VALUES
                         (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

SQL_INSERT_TO_COMMON_DESC = """INSERT INTO common_desc (Type, Season, Sleeve_Length, Sleeve_Type,
                            Sheer, Fit_Type) VALUES (%s,%s,%s,%s,%s,%s)"""
SQL_INSERT_TO_DRESSES = """INSERT INTO dresses (Dresses_Length, Waist_Line, Hem_Shaped, Belt) VALUES (%s,%s,%s,%s)"""
SQL_INSERT_TO_T_SHIRTS = """INSERT INTO t_shirts (Length, Placket_Type, Arabian_Clothing) 
                    VALUES (%s,%s,%s)"""
SQL_INSERT_TO_SWIMWEAR = """INSERT INTO swimwear (Bra, Bottom_Type, Lining, Chest_pad)
                    VALUES (%s,%s,%s,%s)"""
SQL_DRESSES_SEC = 'DRESSES'
SQL_T_SHIRTS_SEC = 'TOPS'
SQL_SWIMWEAR_SEC = 'SWIMWEAR'
GET_WEB_ID = 'ID'
GET_ITEM_ID = 'Item_ID'
SQL_ITEM_ID_QUERY = "SELECT Item_ID FROM products WHERE Web_ID = %s"
SQL_UPDATE_FK_COMMON_DESC = """UPDATE common_desc SET Item_ID = %s ORDER BY Common_Desc_ID DESC LIMIT 1"""
SQL_UPDATE_FK_DRESSES = """UPDATE dresses SET Item_ID = %s Where %s not in (select Item_ID from dresses)
                           ORDER BY Dress_ID  DESC LIMIT 1;"""
SQL_UPDATE_FK_T_SHIRTS = """UPDATE t_shirts SET Item_ID = %s ORDER BY T_Shirt_ID DESC LIMIT 1"""
SQL_UPDATE_FK_SWIMWEAR = """UPDATE swimwear SET Item_ID = %s ORDER BY Swimwear_ID DESC LIMIT 1"""

# sql_db_build file:
SQL_CREATE_DB = "CREATE DATABASE IF NOT EXISTS shein"
SQL_TABLE_PRODUCTS = """CREATE TABLE products(
                    Item_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                    Web_ID CHAR(45),
                    Product_type CHAR(45),
                    Price INTEGER,
                    Average_rating REAL,
                    Reviews_amount CHAR(45),
                    Small CHAR(45),
                    True_to_Size CHAR(45),
                    Large CHAR(45),
                    Style CHAR(45),
                    Color CHAR(45),
                    Pattern_Type CHAR(45),
                    Neckline CHAR(45),
                    Composition CHAR(45),
                    Material CHAR(45),
                    Fabric CHAR(45),
                    Details CHAR(255),
                    Price_ILS REAL,
                    Date_exchange_rate CHAR(45),
                    UNIQUE (Web_ID))"""
SQL_TABLE_DRESSES = """CREATE TABLE dresses(
                    Dress_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                    Item_ID INTEGER UNIQUE,
                    Dresses_Length CHAR(45),
                    Waist_Line CHAR(45),
                    Hem_Shaped CHAR(45),
                    Belt CHAR(45),
                    FOREIGN KEY (Item_ID) REFERENCES products(Item_ID))"""
SQL_TABLE_T_SHIRTS = """CREATE TABLE t_shirts(
                    T_Shirt_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                    Item_ID INTEGER UNIQUE,
                    Length CHAR(45),
                    Placket_Type CHAR(45),
                    Arabian_Clothing CHAR(45),
                    FOREIGN KEY (Item_ID) REFERENCES products(Item_ID)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE)"""
SQL_TABLE_SWIMWEAR = """CREATE TABLE swimwear(
                    Swimwear_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                    Item_ID INTEGER UNIQUE,
                    Bra CHAR(45),
                    Bottom_Type CHAR(45),
                    Lining CHAR(45),
                    Chest_pad CHAR(45),
                    FOREIGN KEY (Item_ID) REFERENCES products(Item_ID)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE)"""
SQL_TABLE_COMMON_DESC = """CREATE TABLE common_desc(
                    Common_Desc_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                    Item_ID INTEGER UNIQUE,
                    Type CHAR(45),
                    Season CHAR(45),
                    Sleeve_Length CHAR(45),
                    Sleeve_Type CHAR(45),
                    Sheer CHAR(45),
                    Fit_Type CHAR(45),
                    FOREIGN KEY (Item_ID) REFERENCES products(Item_ID)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE)"""



