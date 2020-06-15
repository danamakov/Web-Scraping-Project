from bs4 import BeautifulSoup as bs
import requests
import re

# SECTION = "dresses"
# URL = "https://us.shein.com/"
# PRODUCT = "women-dresses"
#
# #create html txt file
# main_page = requests.get(URL)
# main_page_content = main_page.content
# outfile = open("dresses.txt","wb")
# outfile.write(main_page_content)
#
# soup = bs(main_page_content,'html.parser')
#
# #find the dresses section URL
# dresses_url_page = (str(soup.select_one("a[href*="+SECTION+"]" ))).split('"')[3]
#
# #create url adresses for all the dresses products
# dress_page = requests.get(dresses_url_page)
# dress_page_content = dress_page.content
# soup_dress = bs(dress_page_content,'html.parser')
# dress_prod = soup_dress.findall('a', href=True)
# products_url_list = []
# for adress in dress_prod:
#     temp = (str(adress).split('href='))[1]
#     url_prod = temp.split('"')[1]
#     if url_prod.endswith(".html"):
#         products_url_list.append(URL + url_prod)

def product(url):
    html_prod = requests.get(url).content
    soup = bs(html_prod, 'html.parser')

    top_tag_names, top_tag_scores, number_of_posts = [], [], []
    all_info = soup.find("div", {"class": "product-intro__head-price"})
    for tag in all_info.find_all_next("span", {"class": "original"}):
        top_tag_names.append(tag.text)
    print(top_tag_names)
    # user['top tags names'] = top_tag_names
    # for tag in all_info.find_all_next('div', {"class": "grid jc-end ml-auto"}):
    #     top_tag_scores.append(tag.text.replace("\n", " ").split()[1])
    #     number_of_posts.append(tag.text.replace("\n", " ").split()[3])
    # user['top tags scores'] = top_tag_scores
    # user['number of posts'] = number_of_posts
    # del all_info, top_tag_names, top_tag_scores, number_of_posts


product(r"https://eur.shein.com/Allover-Plants-Print-Cami-Dress-p-1239914-cat-1727.html?scici=navbar_2~~tab01navbar05~~5~~real_1727~~SPcCccWomenCategory_default~~0~~0")
# print(url_prod)
# /html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/div[4]/span


