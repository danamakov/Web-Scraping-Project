from bs4 import BeautifulSoup as bs
import requests

SECTION = "dresses"
URL = "https://us.shein.com/"
PRODUCT = "women-dresses"

#create html txt file
main_page = requests.get(URL)
main_page_content = main_page.content
outfile = open("dresses.txt","wb")
outfile.write(main_page_content)

soup = bs(main_page_content,'html.parser')

#find the dresses section URL
dresses_url_page = (str(soup.select_one("a[href*="+SECTION+"]" ))).split('"')[3]
print(dresses_url_page)

#create url adresses for all the dresses products
dress_page = requests.get(dresses_url_page)
dress_page_content = dress_page.content
soup_dress = bs(dress_page_content,'html.parser')
dress_prod = soup_dress.findAll('a', href=True)
products_url_list = []
for adress in dress_prod:
    temp = (str(adress).split('href='))[1]
    url_prod = temp.split('"')[1]
    if url_prod.endswith(".html"):
        products_url_list.append(URL + url_prod)

products_url_list = products_url_list[1:]

