'''
2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
'''


def odd_nums(n):
    """
    :param n: number of generated numbers (количество генерируемых чисел)
    :return: odd numbers from 1 to n (нечетные числа от 1 до n)
    """
    return (i for i in range(1, n + 1, 2))


odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
