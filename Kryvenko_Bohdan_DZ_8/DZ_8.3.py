'''
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...

@type_logger
def calc_cube(x):
   return x ** 3

 a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции?
Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции, например, в виде:
 a = calc_cube(5)
calc_cube(5: <class 'int'>)
'''

from functools import wraps


def type_logger(func):
    @wraps(func) # если эта штука есть то help(calc_cube) показывает коментарий к calc_cube, а если нет то к wrapper
    def wrapper(*args):
        """
         :param args: takes function arguments (принимает аргументы функции)
         :return: type of arguments passed to the function (тип переданых в функцию аргументов)
         """
        for arg in args:
            print(f'{str(func).split()[1]}({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrapper


@type_logger
def calc_cube(*args):
    """
    :param args: number or numbers (число или числа)
    :return: number or numbers to the power of 3 (число или числа в 3 степени)
    """
    return list(map(lambda x: x ** 3, args))


print(calc_cube(7, 2, 3))


help(calc_cube)
