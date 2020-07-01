from bs4 import BeautifulSoup as bs
from data_product import get_data
from creating_DF import make_df
import requests
from tqdm import tqdm

"""
# ITC_project #
web scrapping

In this project we retrive data from the website: https://us.shein.com.
Because the website contains thousands of products, we decide to focus on dresses.
For each dress we gather data as: price, color, rating, style, etc...
For doing so, we used selenium and beautifulsoup packages and wrote the script in python.

Authors: Limor Nunu, Dana Makov
"""

SECTION = "dresses"
URL = "https://us.shein.com/"
PRODUCT = "women-dresses"
NUMBER_OF_PAGES = 2  # The maximum number of pages in the website, you can change this number to lower number.


def main():
    """
    This file get the html of the main page, get into the page of dresses,
    and get a url list of all the dresses in the page.
    The function call the get_html function, and the get_data function.

    return: DataFrame of all the info of each product.
    """

    # create html of main page
    main_page = requests.get(URL).content
    soup = bs(main_page, 'html.parser')

    # find the dresses section URL
    dresses_url_page = (str(soup.select_one("a[href*=" + SECTION + "]"))).split('"')[3]

    products_list = []      # get dict for each product
    total_url_list = []     # get all products url

    for page in tqdm(range(1, NUMBER_OF_PAGES)):
        # changing the pages
        url_page = dresses_url_page + f"&page={page}"

        # create url adresses for all the dresses products in the page
        dress_page = requests.get(url_page).content
        soup_dress = bs(dress_page, 'html.parser')
        dress_prod = soup_dress.findAll('a', href=True)

        products_url_list = []
        for address in dress_prod:
            temp = (str(address).split('href='))[1]
            url_prod = temp.split('"')[1].strip()
            if url_prod.endswith(".html"):
                products_url_list.append(URL + url_prod)

        # list of url for each product
        for url1 in products_url_list[1:-4]:
            total_url_list.append(url1)

    total_url_list = list(set(total_url_list))
    # the first url is the main page of all dresses, so the list start from the 1st item

    # get html and then the info of each product
    for product in tqdm(total_url_list[:10]):
        # print(product)
        try:
            products_list.append(get_data(product))
        except AttributeError:
            pass
        except ValueError:
            pass


    # creating DataFrame
    make_df(products_list)


if __name__ == '__main__':
    main()
