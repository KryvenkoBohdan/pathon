'''
(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не программно);
предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
'''
import os

with open('config.yaml', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split('.')
        if not len(line) > 1:
            if not os.path.exists(*line):
                os.makedirs(*line)
        else:
            line = ','.join(line).replace(',', '.')
            with open(line, 'w', encoding='utf-8') as f:
                f.close()