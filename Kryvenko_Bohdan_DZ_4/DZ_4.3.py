'''
*(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся
в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше
использовать в ответе функции?
'''

from requests import get
from datetime import datetime
from decimal import *


def currency_rates(value):
     """
     :param value: currency code (код валюты)
     :return: the value of the currency in rubles and the date on which this value is relevant (стоимость валюты в рублях и дата в момент которой актуальна эта стоимость )
     """
     value = value.upper()
     response = get('http://www.cbr.ru/scripts/XML_daily.asp').text

     if value not in response:
          return None

     rub = response[(response.find('<Value>', response.find(value))+7) : (response.find('</Value>', response.find(value)))]
     val_date = response[response.find('Date="') + 6 : response.find('" name="')].split('.')
     day, month, year = map(int, val_date)
     return f'{Decimal(rub.replace("," , "."))} , {datetime(day= day, month= month, year=year)}'


if __name__ == '__main__' :
     print(currency_rates('AUD'))
     print(currency_rates('AZN'))
     print(currency_rates('USD'))
     print(currency_rates('EUR'))
     print(currency_rates('eur'))





