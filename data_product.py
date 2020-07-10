from html_soup import get_soup
import configuration as cfg


def soup_find(soup, s_type, class_name):
    """
    :param soup: soup of the page
    :param s_type: string of div or span
    :param class_name: string of the class name
    :return: text of the wanted class in the soup
    """
    return soup.find(s_type, {cfg.CLASS: class_name}).text


def find_all(soup, class_name):
    """
    :param soup: soup of the page
    :param class_name: string of the class name
    :return: text of the wanted elements of the class in the soup
    """
    return soup.find_all(cfg.DIV, {cfg.CLASS: class_name})


def get_data(url):
    """
    :param url: url address of the product
    :return: dict of all the info of the product,
             after call the get_html function to get the soup of the url
    """

    soup = get_soup(url)
    prod_dict = {}

    # adding ID for the product:
    prod_dict[cfg.ID] = soup_find(soup, cfg.DIV, cfg.CLASS_ID).strip().split()[cfg.ID_SPLIT_NUM]

    # adding price for the product:
    prod_dict[cfg.PRICE] = float(soup_find(soup, cfg.DIV, cfg.CLASS_PRICE).split("$")[cfg.PRICE_SPLIT_NUM].strip())

    # adding average rate for the product:
    prod_dict[cfg.RATE] = float(soup_find(soup, cfg.DIV, cfg.CLASS_RATE).strip())

    # adding reviews amount for the product:
    prod_dict[cfg.RVW_AMOUNT] = soup_find(soup, cfg.SPAN, cfg.CLASS_RVW_AMOUNT).strip().split()[cfg.RVW_AMNT_SPLIT_NUM]

    # adding the percentage of product fit to size:
    for sz in find_all(soup, cfg.CLASS_FIT):
        prod_dict[sz.text.split(cfg.FIT_SPLIT_TYPE)[cfg.FIT_FIRST_SPLIT_NUM]] = \
            sz.text.split(cfg.FIT_SPLIT_TYPE)[cfg.FIT_SEC_SPLIT_NUM]

    # adding the description of the product:
    for item in find_all(soup, cfg.CLASS_DESCRIPTION):
        prod_dict[item.text.split(cfg.DESC_SPLIT_TYPE)[cfg.DESC_FIRST_SPLIT_NUM].strip()] = \
            item.text.split(cfg.DESC_SPLIT_TYPE)[cfg.DESC_SEC_SPLIT_NUM].strip()

    return prod_dict


