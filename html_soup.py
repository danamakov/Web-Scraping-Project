from selenium.webdriver.chrome.options import Options
from selenium import webdriver as wb
from bs4 import BeautifulSoup as bs
import configuration as cfg
import time
import os


def get_soup(url):
    """
    :param url: url address
    :return: soup of the html.
    """

    chrome_options = Options()
    chrome_options.add_argument(cfg.HEADLESS)
    # start web browser
    browser = wb.Chrome(executable_path=os.path.abspath(cfg.CHROME_DRIVER), chrome_options=chrome_options)
    # get source code
    browser.get(url)
    html = browser.page_source
    time.sleep(cfg.TIME_SLEEP)
    browser.close()
    return bs(html, cfg.HTML_PARSER)
