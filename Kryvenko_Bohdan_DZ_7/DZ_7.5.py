'''
(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
'''
import json
import os

folder = os.getcwd()
files_list = []

for root, dirs, files in os.walk(folder):
    for file in files:
        file_path = os.path.join(root, file)
        files_list.append((file_path.split('.')[-1], os.stat(file_path).st_size))
max_size = max(files_list, key=lambda x: x[1])[1]

i = 1
size_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    size_dict[i] = (0, [])

for file in files_list:
    num, ext_list = size_dict[10 ** len(str(file[1]))]
    ext_list.append(file[0])
    ext_list = list(set(ext_list))
    size_dict[10 ** len(str(file[1]))] = (num + 1, ext_list)

print(size_dict)

with open(os.path.join(os.getcwd(), 'size_dict.json'), 'w') as f:
    json.dump(size_dict, f)