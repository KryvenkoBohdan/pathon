'''
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
'''

import os

first_dir = 'my_project'
dirs_in_first_dir = ['settings', 'mainapp', 'adminapp', 'authapp']
path = os.path.join(os.getcwd(), first_dir)

if not os.path.exists(path):
    os.mkdir(path)
else:
    print(f'папка с именем: "{first_dir}" уже существует')
for dir in dirs_in_first_dir:
    path = os.path.join(os.getcwd(), first_dir, dir)
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print(f'папка с именем: "{dir}" уже существует в папке: "{first_dir}"')