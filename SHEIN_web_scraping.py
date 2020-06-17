from selenium import webdriver as wb
from bs4 import BeautifulSoup as bs
from data_product import get_data
import pandas as pd
import requests
import time

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


def main():
    """
    This file get the html of the main page, get into the page of dresses,
    and get a url list of all the dresses in the page.
    The function call the get_html function, and the get_data function.

    return: DataFrame of all the info of each product.
    """

    #create html of main page
    main_page = requests.get(URL).content
    soup = bs(main_page,'html.parser')

    #find the dresses section URL
    dresses_url_page = (str(soup.select_one("a[href*="+SECTION+"]" ))).split('"')[3]

    #create url adresses for all the dresses products
    dress_page = requests.get(dresses_url_page).content
    soup_dress = bs(dress_page,'html.parser')
    dress_prod = soup_dress.findAll('a', href=True)

    products_url_list = []
    for adress in dress_prod:
        temp = (str(adress).split('href='))[1]
        url_prod = temp.split('"')[1].strip()
        if url_prod.endswith(".html"):
            products_url_list.append(URL + url_prod)

    #list of url for each product
    products_url_list = list(set(products_url_list[1:]))
    #the first url is the main page of all dresses, so the list start from the 1st item

    products_list = []
    #get html and then the info of each product
    for product in products_url_list:
        products_list.append(get_data(product))

    #creating DataFrame
    prod_df = pd.DataFrame(products_list)
    # with open("test_csv.csv","wb") as file:
    #     file.pd.to_csv(prof_df)
    prod_df.to_csv(r'test_csv.csv')
    print(prod_df)


if __name__ == '__main__':
    main()