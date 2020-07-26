from html_soup import get_soup
from bs4 import BeautifulSoup as bs
from configuration import *
import requests
from tqdm import tqdm
import logging
from exchange_api import exchange_rate, date_exchange_rate
#from sql_insert_products import sql_insert



def soup_find(soup, s_type, class_name):
    """
    :param soup: soup of the page
    :param s_type: string of div or span
    :param class_name: string of the class name
    :return: text of the wanted class in the soup
    """
    return soup.find(s_type, {CLASS: class_name}).text


def find_all(soup, class_name):
    """
    :param soup: soup of the page
    :param class_name: string of the class name
    :return: text of the wanted elements of the class in the soup
    """
    return soup.find_all(DIV, {CLASS: class_name})


def get_data(url, section):
    """
    :param url: url address of the product
    :return: dict of all the info of the product,
             after call the get_html function to get the soup of the url
    """

    soup = get_soup(url)
    prod_dict = {}

    # adding ID for the product:
    prod_dict[ID] = soup_find(soup, DIV, CLASS_ID).strip().split()[ID_SPLIT_NUM]

    # adding price for the product:
    prod_price = float(soup_find(soup, DIV, CLASS_PRICE).split(PRICE_SPLIT_SIGN)[PRICE_SPLIT_NUM].strip())
    prod_dict[PRICE] = prod_price

    # adding average rate for the product:
    prod_dict[RATE] = float(soup_find(soup, DIV, CLASS_RATE).strip())

    # adding reviews amount for the product:
    prod_dict[RVW_AMOUNT] = soup_find(soup, SPAN, CLASS_RVW_AMOUNT).strip().split()[RVW_AMNT_SPLIT_NUM]

    # adding the percentage of product fit to size:
    for sz in find_all(soup, CLASS_FIT):
        prod_dict[sz.text.split(FIT_SPLIT_TYPE)[FIT_FIRST_SPLIT_NUM]] = \
            sz.text.split(FIT_SPLIT_TYPE)[FIT_SEC_SPLIT_NUM]

    # adding the description of the product:
    for item in find_all(soup, CLASS_DESCRIPTION):
        prod_dict[item.text.split(DESC_SPLIT_TYPE)[DESC_FIRST_SPLIT_NUM].strip()] = \
            item.text.split(DESC_SPLIT_TYPE)[DESC_SEC_SPLIT_NUM].strip()

    # adding the price and date from the exchange_api file
    prod_dict[PRICE_EXCHANGE] = exchange_rate * prod_price
    prod_dict[DATE_EXCHANGE] = date_exchange_rate

    #adding product_type by the section:
    prod_dict['Product_type'] = section

    return prod_dict


def product_info(url_choice, num_of_products, section):
    """
    :param url_choice: url of the chosen product (the page of the products)
    :param num_of_products: number of products to scrap
    :param section: chosen section of product (dresses/tops/swimwear)
    :return: call the sql_insert() function after it get all the data for each product (with the function get_data()).
    """

    products_list = []      # get dict for each product
    total_url_list = []     # get all products url

    for page in tqdm(range(1, NUMBER_OF_PAGES)):
        # changing the pages
        url_page = url_choice + PAGE.format(page)

        # create url addresses for all the dresses products in the page
        soup = bs(requests.get(url_page).content, HTML_PRS)
        prod = soup.findAll(URL_FIND_TYPE, href=True)

        products_url_list = []
        for address in prod:
            temp = (str(address).split(URL_SPLIT_SIGN))[TEMP_SPLIT_NUM]
            url_prod = temp.split(URL_PROD_SPLIT_SIGN)[URL_PROD_SPLIT_NUM].strip()
            if url_prod.endswith(HTML_END):
                products_url_list.append(URL + url_prod)

        # list of url for each product
        for url1 in products_url_list[FROM: TO]:
            total_url_list.append(url1)

    total_url_list = list(set(total_url_list))
    # the first url is the main page of all dresses, so the list start from the 1st item

    logging.basicConfig(format='%(asctime)s %(message)s',
                        filename='logging.log', filemode='a')
    logger = logging.getLogger()
    logger.setLevel(logging.NOTSET)

    # get html and then the info of each product
    for product in tqdm(total_url_list[:num_of_products]):
        try:
            products_list.append(get_data(product, section))
        except AttributeError:
            logger.warning(f'There is a problem with the url: {product}')
            pass
        except ValueError:
            logger.warning(f'There is a problem with the url: {product}')
            pass

    # inserting into the database
    return products_list, section
    # sql_insert(products_list, section)
