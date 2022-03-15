'''
5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь к обоим исходным
файлам и путь к выходному файлу со словарём. Проверить работу скрипта для случая, когда все файлы находятся в разных папках.
'''

from sys import exit
from sys import argv
from itertools import zip_longest

with open(argv[1], 'r', encoding='utf-8') as users:
    with open(argv[2], 'r', encoding='utf-8') as hobby:
        user_list = [user.replace(',', ' ').strip() for user in users]
        hobby_list = [i.strip() for i in hobby]
        if len(user_list) >= len(hobby_list):
            with open(argv[3], 'w', encoding='utf-8') as f:
                user_and_hobby = dict(zip_longest(user_list, hobby_list))
                f.write(str(user_and_hobby))
        else:
            exit('1')
        print(user_and_hobby)
