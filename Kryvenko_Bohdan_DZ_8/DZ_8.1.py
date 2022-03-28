'''
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
 email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
 email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
'''

import re

VALID_EMAIL_ADDRESS = re.compile(r'(?P<username>[a-zA-Z0-9_\-\.]+)@(?P<domain>([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5}))')


def email_parse(email_address):
    """
    :param email_address: accepts an email address and checks it for validity
    (принимает имейл адрес и проверяет его на валидность)
    :return: if there is a match, we get a dictionary of the form {'username': '', 'domain': ''}, otherwise we return an error
    (в случае соответствия получаем словарь вида {'username': '', 'domain': ''}, в противном случае возвращаем ошибку)
    """
    result = VALID_EMAIL_ADDRESS.match(email_address)
    try:
        if result:
            result = VALID_EMAIL_ADDRESS.finditer(email_address)
            for el in result:
                return print(el.groupdict())
        else:
            msg = f'wrong email: {email_address}'
            raise ValueError(msg)
    except Exception as error:
        return print(error)


email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')
