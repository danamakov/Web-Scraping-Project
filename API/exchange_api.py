from configuration import *
import requests
from datetime import date

today = date.today()

response = requests.get(f'https://api.ratesapi.io/api/{today}?base={BASE_EX_RATE}&symbols={SYMBOL_EX_RATE}')
data = response.json()
exchange_rate = data[GET_RATE_JASON_EX][SYMBOL_EX_RATE]
date_exchange_rate = data[GET_DATE_JASON_EX]