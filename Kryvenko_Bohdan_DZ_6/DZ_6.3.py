'''
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип:
одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл.
Проверить сохранённые данные.
Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
'''

from sys import exit
from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        user_list = [user.replace(',', ' ').strip() for user in users]
        hobby_list = [i.strip() for i in hobby]
        if len(user_list) >= len(hobby_list):
            with open('user_and_hobby_dict.csv', 'w', encoding='utf-8') as f:
                user_and_hobby = dict(zip_longest(user_list, hobby_list))
                f.write(str(user_and_hobby))
        else:
             exit('1')
        print(user_and_hobby)