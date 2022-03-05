'''
2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с
числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
 num_translate_adv("One")
"Один"
 num_translate_adv("two")
"два"
'''


def num_translate_adv(number):
    """
функция возвращающая значение по заданому ключу, служащая как переводчик чисел от 0 до 10 с английского на русский, с учетом наличия заглавных букв
a function that returns a value by a given key, serving as a translator of numbers from 0 to 10 from English to Russian, taking into account the presence of capital letters
    """
    if number.istitle():
        number = number.lower()
        return number_dict.get(number, 'такого слова нет в словаре').capitalize()
    else:
        return number_dict.get(number, 'такого слова нет в словаре')


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

print(num_translate_adv('one'))
print(num_translate_adv('Two'))
print(num_translate_adv('fsds'))
help(num_translate_adv)