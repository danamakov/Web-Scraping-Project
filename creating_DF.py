import pandas as pd
import os


def make_df(products_list, product_type):
    """
    The function product list.

    return: csv file with the df inside, no duplicates.
    """
    prod_df = pd.DataFrame(products_list)
    if os.path.exists('products.csv') and os.stat('products.csv').st_size != 0:
        prod_df.to_csv('products.csv', mode='a', index=False, header=False)
    else:
        prod_df.to_csv('products.csv', index=False)

    d = pd.read_csv('products.csv')
    d.drop_duplicates(subset=['ID'], inplace=True, keep='first')
    d.to_csv('products.csv', index=False)

