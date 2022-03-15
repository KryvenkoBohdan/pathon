'''
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
'''
import os

folder = os.path.join(os.getcwd(), 'some_data')
for root, dirs, files in os.walk(folder):
    i = 0
    dict_size = {
        100: sum(i + 1 for file in files if os.stat(os.path.join(root, file)).st_size <= 100),
        1000: sum(i + 1 for file in files if 100 < os.stat(os.path.join(root, file)).st_size <= 1000),
        10000: sum(i + 1 for file in files if 1000 < os.stat(os.path.join(root, file)).st_size <= 10000),
        100000: sum(i + 1 for file in files if 10000 < os.stat(os.path.join(root, file)).st_size <= 100000)
    }
print(dict_size)
