from bs4 import BeautifulSoup as bs
import configuration as cfg
from data_product import get_data
import requests
from tqdm import tqdm
import pandas as pd


def product_info(url_choise, num_of_products):
    products_list = []      # get dict for each product
    total_url_list = []     # get all products url

    for page in tqdm(range(1, cfg.NUMBER_OF_PAGES)):
        # changing the pages
        url_page = url_choise + cfg.PAGE.format(page)

        # create url addresses for all the dresses products in the page
        soup = bs(requests.get(url_page).content, cfg.HTML_PRS)
        prod = soup.findAll(cfg.URL_FIND_TYPE, href=True)

        products_url_list = []
        for address in prod:
            temp = (str(address).split(cfg.URL_SPLIT_SIGN))[cfg.TEMP_SPLIT_NUM]
            url_prod = temp.split(cfg.URL_PROD_SPLIT_SIGN)[cfg.URL_PROD_SPLIT_NUM].strip()
            if url_prod.endswith(cfg.HTML_END):
                products_url_list.append(cfg.URL + url_prod)

        # list of url for each product
        for url1 in products_url_list[cfg.FROM: cfg.TO]:
            total_url_list.append(url1)

    total_url_list = list(set(total_url_list))
    # the first url is the main page of all dresses, so the list start from the 1st item

    # get html and then the info of each product
    for product in tqdm(total_url_list[:num_of_products]):
        try:
            products_list.append(get_data(product))
        except AttributeError:
            pass
        except ValueError:
            pass

    # creating DataFrame
    df = pd.DataFrame(products_list)
    print(df)