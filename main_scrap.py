"""
# ITC_project #
web scrapping
In this project we retrieve data from the website: https://us.shein.com.
Because the website contains thousands of products, we decide to focus on dresses, tops and swimwear.
For each product we gather data as: price, color, rating, style, etc...
For doing so, we used selenium and beautifulsoup packages and wrote the script in python.
In this web scrapping YOU can decide which products to scrap, how many products, color and max price.

Authors: Limor Nunu, Dana Makov
"""
from shein import Web_scrap
from data_product import Data_product
from sql_insert_products import Sql_insert_products
from configuration import *
import click
import logging
import datetime


@click.command()
@click.option('--product', '-p', help="""Type 'd' for dresses,
                                        't' for tops,
                                        's' for swimwear""", multiple=False, required=True)
@click.option('--number', '-n', help="""Type the number of products you want to retrieve (This number will 
                                        be the same for each product you chose if you want different number 
                                        please re-run the script)""", type=int, required=True)
@click.option('--color', '-c', default=None, help="""Type ONE color from the list:
                                                    ['Blue', 'Pink', 'Green', 'Red', 'Multi', 'Purple', 'Brown',
                                                     'White', 'Grey', 'Yellow', 'Khaki', 'Black', 'Orange']
                                                     (This color will be the same for each product you chose
                                                     if you want different color please re-run the script.
                                                     It's not mandatory to pick color.""", type=str, required=False)
@click.option('--price', '-$', default=200, help="""Type maximum price.
                                                    The prices are in dollars, no need to write $ sign.""",
              required=False, show_default=True)
def main(product, number, price, color):

    """
    HELP: Welcome to the web scraper =D
    This program retrieves products information from the http://us.shein.com website.
    You can decide which products to scrap, how many products, color and max price.
    """
    logging.basicConfig(format=LOGGING_FORMAT,
                        filename=LOGGING_FILE_NAME, filemode=LOGGING_FILE_MODE)
    logger = logging.getLogger()
    logger.setLevel(logging.NOTSET)
    logger.info(LOGGING_NEW_RUN.format(datetime.datetime.now()))

    # setting the product type
    try:
        if set(product).intersection(PRODUCT_SCRAP_OPT) == set(product):
            prod_to_scrap = product
        else:
            raise ValueError
    except ValueError:
        logger.warning(f"There is a problem with user's input: product type '{product}'")
        print("You entered invalid value for the product type.\n"
              "please type one or more values from the list: ['t', 'd', 's']\n"
              "make sure you put -p before each one of the product type.")

    # setting the number of products to scrap
    try:
        if 0 < int(number) < SCRAP_LIMIT:
            n_to_scrap = int(number)
        else:
            raise ValueError
    except ValueError:
        logger.warning(f"There is a problem with user's input: number of products - '{number}'")
        print("You entered invalid value for the number of products to scrap.\n"
              "please type positive integer less than {}".format(SCRAP_LIMIT))

    # setting the color of product
    try:
        if str(color).capitalize() in COLOR_SCRAP_OPT:
            sort_color = str(color).capitalize()
        elif color is not None:
            raise ValueError
    except ValueError:
        logger.warning(f"There is a problem with user's input: color - '{color}'")
        print("You entered invalid value for the color.\n"
              "please type color from the list: {}".format(COLOR_SCRAP_OPT))
    else:
        sort_color = None

    # setting the max price of products
    try:
        if int(price) > 0:
            sort_max_price = int(price)
        else:
            raise ValueError
    except ValueError:
        print("You entered invalid value for the max price.\n"
              "please type positive integer")
        logger.warning(f"There is a problem with user's input: max price - '{price}'")

    section, num, price, color = SECTION_DICT[prod_to_scrap], n_to_scrap, sort_max_price, sort_color
    url_choice, number, section = Web_scrap.web_scrap(section, num, price, color)
    products_list, section = Data_product.product_info(url_choice, number, section)
    Sql_insert_products.sql_insert(products_list, section)


if __name__ == '__main__':
    """ 
    call the above function 
    """
    main()
