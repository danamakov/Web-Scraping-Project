from df_products import get_data
from selenium import webdriver as wb
import time

chrome = "C:\Limor\Data Science ITC\Web Scraping Project\chromedriver.exe"
url = "https://us.shein.com/Ruffle-Hem-Solid-Cami-Dress-p-1149736-cat-1727.html?" \
      "scici=navbar_2~~tab01navbar05~~5~~real_1727~~SPcCccWomenCategory_default~~0~~0"

def get_html(url, chrome_exe):
    # start web browser
    browser = wb.Chrome(chrome_exe)
    # get source code
    browser.get(url)
    html = browser.page_source
    time.sleep(2)
    browser.close()
    #calling get_data
    return html


url_list = ["https://us.shein.com/Ruffle-Hem-Solid-Cami-Dress-p-1149736-cat-1727.html?scici=navbar_2~~tab01navbar05~~5~~real_1727~~SPcCccWomenCategory_default~~0~~0",
            "https://us.shein.com/Tie-Front-Ruched-Bust-Floral-Bardot-Dress-p-1202505-cat-1727.html?scici=navbar_2~~tab01navbar05~~5~~real_1727~~SPcCccWomenCategory_default~~0~~0",
            "https://us.shein.com/Tie-Shoulder-Solid-Cami-Dress-p-1195493-cat-1727.html?scici=navbar_2~~tab01navbar05~~5~~real_1727~~SPcCccWomenCategory_default~~0~~0"]

list_dict = []
for i in url_list:
    html = get_html(url, chrome)
    prod_dict = get_data(html)
    list_dict.append(prod_dict)

print(list_dict)
"============================================================================================="

# driver = wb.Chrome("C:\Limor\Data Science ITC\Web Scraping Project\chromedriver.exe")
# # driver.get("https://us.shein.com")
#
# from selenium.webdriver.common.action_chains import ActionChains
#
# saveas = ActionChains(driver).key_down(Keys.CONTROL).send_keys('s').key_up(Keys.CONTROL)
# saveas.perform()


# try:
#     close_pop_up1 = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div/div/i")
#     close_pop_up1.click()
# except:
#     pass
# try:
#     close_pop_up2 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/i")
#     close_pop_up2.click()
# except:
#     pass
#
# go_dresses_page = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[9]/div/div[2]/a")
# go_dresses_page.click()
# # dress_page = go_dresses_page.get_attributes("href")
# # print(dress_page)
# try:
#     close_pop_up3 = driver.find_element_by_xpath("/html/body/div[1]/div[10]/div[1]/div/div/i")
#     close_pop_up3.click()
# except:
#     pass
# try:
#     close_pop_up4 = driver.find_element_by_xpath("/html/body/div[11]/div[1]/i")
#     close_pop_up4.click()
# except:
#     pass
#
# get_product_list = driver.find_elements_by_class_name("$x(“//div[@class=‘iconfont icon’]/a[contains(@class,"
#                                                       "‘xaction-open-trips’)]“)")
# get_product_list.click()
#
# print(get_product_list)

# iconfont icon
#
# c-goodsitem__ratiowrap