'''
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи.
'''


def num_translate(key):
    """
    функция возвращающая значение по зананому ключу, служащая как переводчик чисел от 0 до 10 с английского на русский
    a function that returns a value by a given key, serving as a translator of numbers from 0 to 10 from English to Russian
    """
    return number_dict.get(key)


number_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыри',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восем',
    'nine': 'девять',
    'ten': 'десять'
}

print(num_translate('two'))
print(num_translate('jhk'))
