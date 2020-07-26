from bs4 import BeautifulSoup as bs
from configuration import *
import requests


class Web_scrap:

    @staticmethod
    def web_scrap(SECTION, number, PRICE, COLOR=None):
        """
        :param SECTION: the user's chosen product type (DRESSES, TOPS, SWIMWEAR)
        :param number: number of products to scrap
        :param PRICE: max price of products
        :param COLOR: color of products
        :return: url according to the user's choice, number of products and section
        This function use the html of the main page, get into the page of chosen product (DRESSES, TOPS,
        SWIMWEAR) and the user's choices: number of products, max price and color of product.
        This function create list of url for the product, and call the product_info() function in order to get the info
         for each product in the list.
        """

        # create html of main page
        soup = bs(requests.get(URL).content, HTML_PRS)

        # find the section URL
        products_url_page = str(soup.find(URL_PAGE_FIND_TYPE,
                                          {URL_PAGE_TITLE: SECTION})
                                ).split(PRODUCT_URL_PAGE_SPLIT)[PRODUCT_URL_PAGE_SPLIT_NUM]

        # create html of products page (by the section)
        soup = bs(requests.get(products_url_page).content, HTML_PRS)

        if COLOR is not None:
            # find all the url of the product by different colors
            prod_color = str(soup.find_all(PROD_COLOR_SPAN,
                                           {PROD_COLOR_CLASS: PROD_COLOR_CLASS_NAME})
                             ).split(PROD_COLOR_SPLIT_SIGN)
            all_url = []
            for y in [x.split() for x in prod_color if HREF in x]:
                all_url.append(URL + " ".join([x.split(HREF) for x in y if HREF in x]
                                                  [LOOP_COLOR_NUM]).strip().strip(STRIP_SIGN))

            # create dict of colors and the url by color
            color_dict = dict(zip(COLORS_LIST, all_url))

            # create the url by the price range
            url_choice = color_dict[COLOR] + URL_CHOICE_PRICE.format(str(LOW_PRICE), str(PRICE))

        else:
            url_choice = URL + products_url_page + URL_CHOICE_PRICE.format(str(LOW_PRICE), str(PRICE))

        return url_choice, number, SECTION
