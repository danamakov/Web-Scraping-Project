from selenium.webdriver.chrome.options import Options
from selenium import webdriver as wb
from bs4 import BeautifulSoup as bs
import time
import os


def get_html(url, *args):
    """
    The function get url.
    return: soup of the html.
    """

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # start web browser
    browser = wb.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=chrome_options)
    # get source code
    browser.get(url)
    html = browser.page_source
    time.sleep(2)
    browser.close()
    soup = bs(html, 'html.parser')

    return soup