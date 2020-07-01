from bs4 import BeautifulSoup as bs
from selenium_html import get_html



def get_data(url):
    """
    The function get url of product,
    call the get_html function to get the html of the url.

    return: dict of all the info of the product.
    """

    # convert the url into html:
    content = get_html(url)
    soup = bs(content, 'html.parser')

    prod_dict = {}

    # adding ID for the product:
    item_id = soup.find("div", {"class": "product-intro__head-sku"}).text.strip().split()[1]
    prod_dict["ID"] = item_id

    # adding price for the product:
    price = float(soup.find("div", {"class": "product-intro__head-price"}).text.split("$")[1].strip())
    prod_dict["price"] = price

    # adding average rate for the product:
    average_rating = float(soup.find("div", {"class": "ave-rate"}).text.strip())
    prod_dict["average_rating"] = average_rating

    # adding reviews amount for the product:
    reviews_amount = soup.find("span", {"class": "product-intro__head-reviews-text color-blue-text"}).text.strip().split()[0]
    prod_dict["reviews_amount"] = reviews_amount

    # adding the percentage of product fit to size:
    for sz in soup.find_all("div", {"class": "fit-item"}):
        prod_dict[sz.text.split("  ")[0]] = sz.text.split("  ")[1]

    # adding the description of the product:
    for item in soup.find_all("div", {"class": "product-intro__description-table-item"}):
        prod_dict[item.text.split(":")[0].strip()] = item.text.split(":")[1].strip()

    return prod_dict


