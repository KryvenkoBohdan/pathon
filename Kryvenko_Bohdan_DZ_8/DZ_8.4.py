'''
4. Написать декоратор с аргументом-функцией (callback),
позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...
@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

 a = calc_cube(5)
125
 a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
'''

from functools import wraps


def val_checker(func):
    @wraps(func)  # если эта штука есть то help(calc_cube) показывает коментарий к calc_cube, а если нет то к wrapper
    def wrapper(arg):
        """
        :param arg: takes a function argument and checks for validity
        (принимает аргумент функции и проверяет валидность)
        :return: if the argument is invalid, the nested function is executed otherwise an error is generated
        (в случае валидности агрумента выполняется вложеная функция в противном случае генерируется ошибка)
        """
        if not func(arg) < 0:
            return func(arg)
        else:
            raise ValueError(f'wrong val {arg}')

    return wrapper


@val_checker
def calc_cube(x):
    """
    :param x: number (число)
    :return: number to the power of 3 (число в 3 степени)
    """
    return x ** 3


help(calc_cube)
print(calc_cube(5))
print(calc_cube(-5))
