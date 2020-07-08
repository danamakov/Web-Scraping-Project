from bs4 import BeautifulSoup as bs
from data_product import get_data
import configuration as cfg
import requests
from tqdm import tqdm
import pandas as pd


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
    This file get the html of the main page, get into the page of dresses,
    and get a url list of all the dresses in the page.
    The function call the get_html function, and the get_data function.
    return: DataFrame of all the info of each product.
    """

    # create html of main page
    soup = bs(requests.get(cfg.URL).content, 'html.parser')

    # find the section URL
    products_url_page = str(soup.find("a", {"title": cfg.SECTION})).split('"')[3]

    # create html of products page (by the section)
    soup = bs(requests.get(products_url_page).content, 'html.parser')

    # find all the url of the product by different colors
    tops_color = str(soup.find_all("span", {"class": "attr-item-pic j-attr-item"})).split('>')
    all_url = []
    for y in [x.split() for x in tops_color if 'href="' in x]:
        all_url.append(cfg.URL + " ".join([x.split('href="') for x in y if 'href="' in x][0]).strip().strip('"'))

    # create dict of colors and the url by color
    color_dict = dict(zip(cfg.COLORS_LIST, all_url))

    # create the url by the price range
    url_choise = color_dict[cfg.COLOR] + f'?currency=USD&min_price={str(cfg.LOW_PRICE)}&max_price={str(cfg.HIGH_PRICE)}'

    products_list = []      # get dict for each product
    total_url_list = []     # get all products url

    for page in tqdm(range(1, cfg.NUMBER_OF_PAGES)):
        # changing the pages
        url_page = url_choise + f"&page={page}"

        # create url addresses for all the dresses products in the page
        soup = bs(requests.get(url_page).content, 'html.parser')
        prod = soup.findAll('a', href=True)

        products_url_list = []
        for address in prod:
            temp = (str(address).split('href='))[1]
            url_prod = temp.split('"')[1].strip()
            if url_prod.endswith(".html"):
                products_url_list.append(cfg.URL + url_prod)

        # list of url for each product
        for url1 in products_url_list[1:-4]:
            total_url_list.append(url1)

    total_url_list = list(set(total_url_list))
    # the first url is the main page of all dresses, so the list start from the 1st item

    # get html and then the info of each product
    for product in tqdm(total_url_list[:3]):
        try:
            products_list.append(get_data(product))
        except AttributeError:
            pass
        except ValueError:
            pass

    # creating DataFrame
    df = pd.DataFrame(products_list)
    print(df)


if __name__ == '__main__':
    main()