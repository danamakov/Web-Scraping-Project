from selenium import webdriver as wb
import time


def get_html(url, *args):
    """
    The function get url.

    return: html.
    """

    # start web browser
    browser = wb.Chrome()
    # get source code
    browser.get(url)
    html = browser.page_source
    time.sleep(2)
    browser.close()

    return html
