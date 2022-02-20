'''
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
(по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
'''
from random import choice


def get_jokes(number_of_jokes, any_list_1, any_list_2, any_list_3, flag = True):
    """
    :param number_of_jokes: the required number of jokes
    необходимое количество шуток
    :param any_list_1: any list containing the words needed to generate the joke
    любой список содержащий слова необходимые для генерирования шутки
    :param any_list_2: any list containing the words needed to generate the joke
    любой список содержащий слова необходимые для генерирования шутки
    :param any_list_3: any list containing the words needed to generate the joke
    любой список содержащий слова необходимые для генерирования шутки
    :param flag: flag with value True (no word repetition limit) or False (word repetition limited)
    флаг со значением True (нет ограничения по повторению слов) или False (повторение слов ограничено)
    :return: a list of the specified number of jokes
    список из указаного количества шуток
    """
    result_list = []
    i = 1
    if flag:
        while i <= int(number_of_jokes):
            result = f'{choice(any_list_1)} {choice(any_list_2)} {choice(any_list_3)}'
            result_list.append(result)
            i += 1
        return result_list
    else:
        while i <= int(number_of_jokes) and any_list_1 or any_list_2 or any_list_3:
            a = choice(any_list_1)
            b = choice(any_list_2)
            c = choice(any_list_3)
            result = f'{a} {b} {c}'
            result_list.append(result)
            any_list_1.remove(a)
            any_list_2.remove(b)
            any_list_3.remove(c)
            i += 1
        return result_list


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(10, nouns, adverbs, adjectives))
print(get_jokes(10, nouns, adverbs, adjectives, flag=False))
