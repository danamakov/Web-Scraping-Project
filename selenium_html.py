from selenium.webdriver.chrome.options import Options
from selenium import webdriver as wb
import time
import os


def get_html(url, *args):
    """
    The function get url.
    return: html.
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

    return html
