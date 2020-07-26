from selenium.webdriver.chrome.options import Options
from selenium import webdriver as wb
from bs4 import BeautifulSoup as bs
from configuration import *
import time
import os


class Html_soup:
    @staticmethod
    def get_soup(url):
        """
        :param url: url address
        :return: soup of the html.
        """

        chrome_options = Options()
        chrome_options.add_argument(HEADLESS)
        # start web browser
        browser = wb.Chrome(executable_path=os.path.abspath(CHROME_DRIVER), chrome_options=chrome_options)
        # get source code
        browser.get(url)
        html = browser.page_source
        time.sleep(TIME_SLEEP)
        browser.close()
        return bs(html, HTML_PARSER)
