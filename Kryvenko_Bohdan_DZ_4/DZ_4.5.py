'''
*(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
> python task_4_5.py USD
75.18, 2020-09-05
'''
from requests import get
from datetime import datetime
from decimal import *
from sys import argv


value = argv[1]
value = value.upper()
response = get('http://www.cbr.ru/scripts/XML_daily.asp').text

if value not in response:
    print (None)

rub = response[(response.find('<Value>', response.find(value))+7) : (response.find('</Value>', response.find(value)))]
val_date = response[response.find('Date="') + 6 : response.find('" name="')].split('.')
day, month, year = map(int, val_date)
print(f'{Decimal(rub.replace("," , "."))} , {datetime(day= day, month= month, year=year)}')