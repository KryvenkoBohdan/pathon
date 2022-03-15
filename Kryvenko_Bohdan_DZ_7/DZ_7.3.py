'''
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
это реальная задача, которая решена, например, во фреймворке django.
'''
import os
import shutil

templates_folder = os.path.join(os.getcwd(), 'my_project', 'templates')
if not os.path.exists(templates_folder):
    os.mkdir(templates_folder)

folder = os.path.join(os.getcwd(), 'my_project')
files_List = []

for root, dirs, files in os.walk(folder):
     for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            files_List.append(file_path)

for path in files_List:
    folder = os.path.join(templates_folder, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, save_path)



