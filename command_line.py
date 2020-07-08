import click

PRODUCT_SCRAP_OPT = {'t', 'a', 'd', 's', 'T', 'A', 'D', 'S'}
SCRAP_LIMIT = 1000
COLOR_SCRAP_OPT = ['Blue', 'Pink', 'Green', 'Red', 'Multi', 'Purple', 'Brown', 'White',
                       'Grey', 'Yellow', 'Khaki', 'Black', 'Orange']


@click.command()
@click.option('--product', '-p', help="Type 'd' for dresses,\n 't' for tops,\n 's' for swimwear,\n 'a' for all\n"\
                                      "you can choose multiple products if you want.\n"
                                      "to choose multiple values please type -p before each", multiple=True,
              required=True)

@click.option('--number','-n', help="Type the number of products you want to retrieve\n"
                                    "(This number will be the same for each product you chose\n"
                                    "if you want different number please re-run the script.", type=int, required=True)

@click.option('--color','-c', default=None, help="Type ONE color from the list:"\
              "['Blue', 'Pink', 'Green', 'Red', 'Multi', 'Purple', 'Brown', 'White', 'Grey', 'Yellow', 'Khaki',"
              " 'Black', 'Orange']\n"
              "(This color will be the same for each product you chose\n"
              "if you want different color please re-run the script.\n It's not mandatory to pick color.",
              type=str, required=False)

@click.option('--price','-$',default=200,
               help='Type maximum price.\n' \
                    'The prices are in dollars, no need to write $ sign',
               required=False, show_default=True)


def main(product, number, color, price):
    """
    HELP: Welcome to the web scraper =D
    This program retrieves products information from the http://us.shein.com website.
    You can decide which products to scrap, how many products, color and max price.
    """
    try:
        if set(product).intersection(PRODUCT_SCRAP_OPT) == set(product):
            prod_to_scrap = product
        else:
            raise ValueError
    except ValueError:
        print("You entered invalid value for the product type.\n"
              "please type one or more values from the list: ['t', 'a', 'd', 's']\n"
              "make sure you put -p before each one of the product type.")

    try:
        if 0 < int(number) < SCRAP_LIMIT:
            n_to_scrap = int(number)
        else:
            raise ValueError
    except ValueError:
        print("You entered invalid value for the number of products to scrap.\n"
              "please type positive integer less than {}".format(SCRAP_LIMIT))

    try:
        if color.title() in COLOR_SCRAP_OPT:
            sort_color = color.title()
        else:
            raise ValueError
    except ValueError:
        print("You entered invalid value for the color.\n"
              "please type color from the list: {}".format(COLOR_SCRAP_OPT))

    try:
        if int(price) > 0:
            sort_max_price = int(price)
        else:
            raise ValueError
    except ValueError:
        print("You entered invalid value for the max price.\n"
              "please type positive integer")



if __name__ == '__main__':
    main()


