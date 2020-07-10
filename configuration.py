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

# # user selection:
# SECTION = "DRESSES"     #TOPS, SWIMWEAR, DRESSES
# HIGH_PRICE = 15          # max 100
# COLOR = 'Blue'           # by COLOR_LIST


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
HERF = 'href="'
STRIP_SIGN = '"'
LOOP_COLOR_NUM = 0
URL_CHOISE_PRICE = '?currency=USD&min_price={}&max_price={}'


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
CLASS_PRICE = "product-intro__head-price"
PRICE_SPLIT_NUM = 1
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
