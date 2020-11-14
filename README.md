# ITC PROJECT
### web scrapping!

In this project we retrive data from the website: 
#### https://us.shein.com
The website contains thousands of products, we decided to focus on dresses, tops and swimwear.
For each product we gather data as: price, color, rating, style, etc...
For doing so, we used selenium and beautifulsoup packages and wrote the script in python.

### Installation Requirements
Please install requirements.txt file, and also all the files attached.
```sh
beautifulsoup4==4.9.1
certifi==2020.4.5.1
chardet==3.0.4
click==7.1.2
Flask==1.1.2
idna==2.9
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
python-dateutil==2.8.1
pytz==2020.1
regex==2020.6.8
requests==2.23.0
selenium==3.141.0
six==1.15.0
soupsieve==2.0.1
tqdm==4.47.0
urllib3==1.25.9
Werkzeug==1.0.1
wincertstore==0.2
tqdm==4.47.0
```

# New Features!

  - Web scrap from your CLI.
  - Choose your own preferences in scrapping.
  - Add your products into database.
  - Get the price exchange rate (to NIS) for each product using API.

### Tech

The files and functions in it:

* [main_scrap] - this is the file you want to use from your CLI.
* [shein] - awesome web-scrap function that call to the product_info() function and return url according to the user's choice, number of products and section.
* [html_soup] - with the function get_soup() it can return the html that you're looking for, as a text.
* [data_product] - get the data for each product, using the soup_find(), find_all(), product_info() and get_data().
* [exchange_api] - get price exchange rate by API.
* [configuration] - including all the constants.
* [sql_db_build] - create the database, this file used only once in order to create the DB. You should run this file before scraping.
* [sql_insert_products] - insert all the product's info to the database.
* [logging.log] - log file (contains errors and run info).

### How to run the program:
Type in the terminal for some help with this web scarper:
```sh
python main_scrap.py --help
```

Type your choices (example):
```sh
python main_scrap.py -p t -n 5 -c pink -$ 30
```
#### This will scrap:

> -p t ---> for TOPS
> -n 5 ---> for scrap 5 products
> -c pink ---> for pink products (optional)
> -$ 30 ---> for limit the max price to 30$ (optional)

### Links

You can use the links below to get to the GitHub page of the project, or to the submission on Hive:

| Plugin | LINK |
| ------ | ------ |
| GitHub | https://github.com/danamakov/ITC_project.git |
| Hive | https://lms.itc.tech/ |


### Team
- Limor Nunu
- Dana Makov
