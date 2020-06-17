from bs4 import BeautifulSoup as bs
import requests
import selenium
from selenium import webdriver as wb
import urllib.request
from urllib.request import Request, urlopen

req = Request('https://us.shein.com/')
html = urlopen(req).read()
print(html)

# driver = wb.Chrome(r"C:\Users\user\PycharmProjects\ITC_project\chromedriver.exe")
# driver.get('https://us.shein.com/')
# click_pop = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div/div/i').click()
# click_odresses = driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div[1]/div/div[2]/div[2]/div/div[5]/a').click()
# click_obj = driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div[1]/div/div[2]/div[2]/div/div[5]/a').click()



