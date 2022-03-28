'''
2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
для получения информации вида:
(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
'''

import re

remote_addr = re.compile(r'\d+\.\d+\.\d+\.\d+')
request_datetime = re.compile(r'\d+.\w+.\d+\:\d+\:\d+\:\d+\s\+\d+')
request_type = re.compile(r'[A-Z]{3}\s')
requested_resource = re.compile(r'\s\/\w+\/\w+\s')
response_code = re.compile(r'\s\d+\s')
response_size = re.compile(r'\d+\s\"')

with open('nginx_logs.txt', encoding='utf-8') as f:
    raw = f.readline().strip()
    for raw in f:
        parsed_raw = (
            (*(el.group() for el in remote_addr.finditer(raw))),
            (*(el.group() for el in request_datetime.finditer(raw))),
            (*(el.group() for el in request_type.finditer(raw))),
            (*(el.group() for el in requested_resource.finditer(raw))),
            (*(el.group() for el in response_code.finditer(raw))),
            (str(*(el.group() for el in response_size.finditer(raw))).split()[0])
        )
        print(parsed_raw)