# ITC PROJECT
### web scrapping!

In this project we retrive data from the website: 
#### https://us.shein.com
 [![Build Status](http://cdn.parcelsapp.com/assets/landing/carriers/shein-208ca201157daf4e9f330022e23deb4cdacdbecba8f2a57a946a4e9f4060d33c.jpg)](https://travis-ci.org/joemccann/dillinger)
 
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
pandas==1.0.4
python-dateutil==2.8.1
pytz==2020.1
regex==2020.6.8
requests==2.23.0
six==1.15.0
soupsieve==2.0.1
urllib3==1.25.9
Werkzeug==1.0.1
wincertstore==0.2
tqdm==4.47.0
```

# New Features!

  - Web scrap from your CLI.
  - Choose your own preferences in scrapping.
  - Add your products into database.

### Tech

The files and functions in it:

* [command_line] - this is the file you want to use from your CLI, it calls the web_scrap() function.
* [shein] - awesome web-scrap function that call to the product_info() function.
* [html_soup] - with the function get_soup() it can return the html that you're looking for, as a text.
* [data_product] - get the data for each product, using the soup_find(), find_all(), product_info() and get_data().
* [configuration] - including all the constants.
* [sql_db_build] - create the database, this file used only once in order to create the DB.
* [sql_insert_products] - insert all the product's info to the database.
* [logging.log] - log file (contains errors and run info).

### How to run the program:
Type in the terminal for some help with this web scarper:
```sh
python command_line.py --help
```

Type your choices (example):
```sh
python command_line.py -p t -n 5 -c pink -$ 30
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

