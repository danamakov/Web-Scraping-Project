from shein import web_scrap
import configuration as cfg
import click


@click.command()
@click.option('--product', '-p', help="""Type 'd' for dresses,
                                        't' for tops,
                                        's' for swimwear""", multiple=False, required=True)
@click.option('--number', '-n', help="""Type the number of products you want to retrieve (This number will 
                                        be the same for each product you chose if you want different number 
                                        please re-run the script)""", type=int, required=True)
@click.option('--color', '-c', default=None, help="""Type ONE color from the list:
                                                    ['Blue', 'Pink', 'Green', 'Red', 'Multi', 'Purple', 'Brown',
                                                     'White', 'Grey', 'Yellow', 'Khaki', 'Black', 'Orange']
                                                     (This color will be the same for each product you chose
                                                     if you want different color please re-run the script.
                                                     It's not mandatory to pick color.""", type=str, required=False)
@click.option('--price', '-$', default=200, help="""Type maximum price.
                                                    The prices are in dollars, no need to write $ sign.""",
              required=False, show_default=True)
def cli(product, number, price, color):
    """
    HELP: Welcome to the web scraper =D
    This program retrieves products information from the http://us.shein.com website.
    You can decide which products to scrap, how many products, color and max price.
    """
    try:
        if set(product).intersection(cfg.PRODUCT_SCRAP_OPT) == set(product):
            prod_to_scrap = product
        else:
            raise ValueError
    except ValueError:
        print("You entered invalid value for the product type.\n"
              "please type one or more values from the list: ['t', 'a', 'd', 's']\n"
              "make sure you put -p before each one of the product type.")

    try:
        if 0 < int(number) < cfg.SCRAP_LIMIT:
            n_to_scrap = int(number)
        else:
            raise ValueError
    except ValueError:
        print("You entered invalid value for the number of products to scrap.\n"
              "please type positive integer less than {}".format(cfg.SCRAP_LIMIT))

    try:
        if str(color).capitalize() in cfg.COLOR_SCRAP_OPT:
            sort_color = str(color).capitalize()
        elif color is not None:
            raise ValueError
    except ValueError:
        print("You entered invalid value for the color.\n"
              "please type color from the list: {}".format(cfg.COLOR_SCRAP_OPT))
    else:
        sort_color = None

    try:
        if int(price) > 0:
            sort_max_price = int(price)
        else:
            raise ValueError
    except ValueError:
        print("You entered invalid value for the max price.\n"
              "please type positive integer")

    web_scrap(cfg.SECTION_DICT[prod_to_scrap], n_to_scrap, sort_max_price, sort_color)


if __name__ == '__main__':
    cli()
