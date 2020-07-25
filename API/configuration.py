"""
A file with all const variables.
In order to change their value it must be changed in this file
"""

# command line constants:
PRODUCT_SCRAP_OPT = {'t', 'a', 'd', 's', 'T', 'A', 'D', 'S'}
SCRAP_LIMIT = 1000
COLOR_SCRAP_OPT = ['Blue', 'Pink', 'Green', 'Red', 'Multi', 'Purple', 'Brown', 'White',
                       'Grey', 'Yellow', 'Khaki', 'Black', 'Orange']
SECTION_DICT = {'t': 'TOPS', 'd': 'DRESSES', 's': 'SWIMWEAR'}


# exchange_api constants:
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
COL_P_DATE_EXCHANGE = 'Date_exchange_rate'
COL_P_PRICE_EXCHANGE = 'Price_ILS'
PRODUCT_COL_LIST = [COL_P_WEB_ID, COL_P_PRODUCT_TYPE, COL_P_PRICE, COL_P_AVERAGE_RATING, COL_P_REVIEWS_AMOUNT,
                    COL_P_SMALL, COL_P_TRUE_TO_SIZE, COL_P_LARGE, COL_P_STYLE, COL_P_COLOR, COL_P_PATTERN_TYPE,
                    COL_P_NECKLINE, COL_P_COMPOSITION, COL_P_MATERIAL, COL_P_FABRIC, COL_P_DATE_EXCHANGE,
                    COL_P_PRICE_EXCHANGE]


## dresses table
COL_D_WEB_ID = 'ID'
COL_D_DRESS_LENGTH = 'Dresses Length'
COL_D_TYPE = 'Type'
COL_D_DETAILS = 'Details'
COL_D_SLEEVE_LENGTH = 'Sleeve Length'
COL_D_SEASON = 'Season'
COL_D_WAIST_LINE = 'Waist Line'
COL_D_SHEER = 'Sheer'
COL_D_HEM_SHAPED = 'Hem Shaped'
COL_D_FIT_TYPE = 'Fit Type'
COL_D_BELT = 'Belt'
COL_D_SLEEVE_TYPE = 'Sleeve Type'
COL_D_LINING = 'Lining'
DRESSES_COL_LIST = [COL_D_WEB_ID, COL_D_DRESS_LENGTH, COL_D_TYPE, COL_D_DETAILS, COL_D_SLEEVE_LENGTH, COL_D_SEASON,
                    COL_D_WAIST_LINE, COL_D_SHEER, COL_D_HEM_SHAPED, COL_D_FIT_TYPE, COL_D_BELT, COL_D_SLEEVE_TYPE,
                    COL_D_LINING]

## T-shirts/tops table
COL_T_WEB_ID = 'ID'
COL_T_LENGTH = 'Length'
COL_T_TYPE = 'Type'
COL_T_DETAILS = 'Details'
COL_T_SEASON = 'Season'
COL_T_SHEER = 'Sheer'
COL_T_FIT_TYPE = 'Fit Type'
COL_T_SLEEVE_LENGTH = 'Sleeve Length'
COL_T_SLEEVE_TYPE = 'Sleeve Type'
COL_T_PLACKET_TYPE = 'Placket Type'
COL_T_ARABIAN_CLOTHING = 'Arabian Clothing'
TSHIRTS_COL_LIST = [COL_T_WEB_ID, COL_T_LENGTH, COL_T_TYPE, COL_T_DETAILS, COL_T_SEASON, COL_T_SHEER, COL_T_FIT_TYPE,
                    COL_T_SLEEVE_LENGTH, COL_T_SLEEVE_TYPE, COL_T_PLACKET_TYPE, COL_T_ARABIAN_CLOTHING]

## swimwear table
COL_S_WEB_ID = 'ID'
COL_S_DETAILS = 'Details'
COL_S_BRA_TYPE = 'Bra Type'
COL_S_BOTTOM_TYPE = 'Bottom Type'
COL_S_LINING = 'Lining'
COL_S_CHEST_PAD = 'Chest pad'
SWIMWEAR_COL_LIST = [COL_S_WEB_ID, COL_S_DETAILS, COL_S_BRA_TYPE, COL_S_BOTTOM_TYPE,
                     COL_S_LINING, COL_S_CHEST_PAD]
