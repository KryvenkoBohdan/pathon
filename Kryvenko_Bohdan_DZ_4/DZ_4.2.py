'''
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере,
посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать
результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты,
которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан
аргумент? В качестве примера выведите курсы доллара и евро.
'''

from requests import get
from decimal import *


def currency_rates(value):
     """
     :param value: currency code (код валюты)
     :return: the value of the currency in rubles  (стоимость валюты в рублях)
     """
     value = value.upper()
     response = get('http://www.cbr.ru/scripts/XML_daily.asp').text

     if value not in response:
          return None

     rub = response[(response.find('<Value>', response.find(value))+7) : (response.find('</Value>', response.find(value)))]

     return f'{Decimal(rub.replace("," , "."))}'


if __name__ == '__main__' :
     print(currency_rates('USD'))
     print(currency_rates('EUR'))
     print(currency_rates('eur'))