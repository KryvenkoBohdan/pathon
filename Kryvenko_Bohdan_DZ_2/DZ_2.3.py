'''
3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
Эта задача намного серьёзнее, чем может сначала показаться.
'''

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in my_list:
    if i.isdigit():
        i = f'"{i.zfill(2)}"'
    elif i.startswith('+'):
        i = f'"{"+" + (i.lstrip("+").zfill(2))}"'
    print(i, end = ' ')







