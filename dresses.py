from bs4 import BeautifulSoup as bs
import requests

SECTION = "dresses"
URL = "https://us.shein.com/"

main_page = requests.get(URL)
main_page_content = main_page.content
outfile = open(r"C:\Users\user\Documents\ITC\Project/dresses.txt","wb")
outfile.write(main_page_content)

soup = bs(main_page_content,'html.parser')
class_title = "dresses"

dresses_url_page = (str(soup.select_one("a[href*="+SECTION+"]" ))).split('"')[3]
print(dresses_url_page)

