from configuration import *
import requests
from datetime import date
"""
This file get price exchange rate by API.
"""

today = date.today()

response = requests.get(API_REQUEST.format(today, BASE_EX_RATE, SYMBOL_EX_RATE))
data = response.json()
exchange_rate = data[GET_RATE_JASON_EX][SYMBOL_EX_RATE]
date_exchange_rate = data[GET_DATE_JASON_EX]
