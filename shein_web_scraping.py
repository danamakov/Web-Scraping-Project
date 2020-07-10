from bs4 import BeautifulSoup as bs
from products import product_info
import configuration as cfg
import requests


"""
# ITC_project #
web scrapping
In this project we retrive data from the website: https://us.shein.com.
Because the website contains thousands of products, we decide to focus on dresses.
For each dress we gather data as: price, color, rating, style, etc...
For doing so, we used selenium and beautifulsoup packages and wrote the script in python.
Authors: Limor Nunu, Dana Makov
"""


def main():
    """
    This file get the html of the main page, get into the page of chosen product (DRESSES, TOPS, SWIMWEAR),
    and get a url list of all the products.
    The function call the get_html function, and the get_data function.
    :return: DataFrame of all the info of each product.
    """

    # create html of main page
    soup = bs(requests.get(cfg.URL).content, cfg.HTML_PRS)

    # find the section URL
    products_url_page = str(soup.find(cfg.URL_PAGE_FIND_TYPE,
                                      {cfg.URL_PAGE_TITLE: cfg.SECTION})
                            ).split(cfg.PRODUCT_URL_PAGE_SPLIT)[cfg.PRODUCT_URL_PAGE_SPLIT_NUM]

    # create html of products page (by the section)
    soup = bs(requests.get(products_url_page).content, cfg.HTML_PRS)

    # find all the url of the product by different colors
    prod_color = str(soup.find_all(cfg.PROD_COLOR_SPAN,
                                   {cfg.PROD_COLOR_CLASS: cfg.PROD_COLOR_CLASS_NAME})
                     ).split(cfg.PROD_COLOR_SPLIT_SIGN)
    all_url = []
    for y in [x.split() for x in prod_color if cfg.HERF in x]:
        all_url.append(cfg.URL + " ".join([x.split(cfg.HERF) for x in y if cfg.HERF in x]
                                          [cfg.LOOP_COLOR_NUM]).strip().strip(cfg.STRIP_SIGN))

    # create dict of colors and the url by color
    color_dict = dict(zip(cfg.COLORS_LIST, all_url))

    # create the url by the price range
    url_choise = color_dict[cfg.COLOR] + cfg.URL_CHOISE_PRICE.format(str(cfg.LOW_PRICE), str(cfg.HIGH_PRICE))

    product_info(url_choise, 3)


if __name__ == '__main__':
    main()