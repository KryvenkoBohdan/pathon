'''1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...
'''


def odd_nums(n):
    """
    :param n: number of generated numbers (количество генерируемых чисел)
    :return: odd numbers from 1 to n (нечетные числа от 1 до n)
    """
    for i in range(1, n + 1, 2):
        yield i


odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))