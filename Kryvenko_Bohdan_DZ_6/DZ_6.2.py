'''
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
'''
from collections import Counter

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    result = []
    for line in f:
        pars_line = line.split()
        result.append(pars_line[0])

spamer = Counter(result).most_common()
print('IP адрес спамера:', spamer[0][0])