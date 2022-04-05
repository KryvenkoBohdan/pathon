'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном
виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
'''


class Matrix:
    def __init__(self, list_in_list):
        self.list_in_list = list_in_list

    def __str__(self):
        return '\n'.join([' '.join(map(str, el)) for el in self.list_in_list])

    def __add__(self, other):
        result = []
        if len(self.list_in_list) == len(other.list_in_list):
            for list1, list2 in zip(self.list_in_list, other.list_in_list):
                if len(list1) == len(list2):
                    res = [i + j for i, j in zip(list1, list2)]
                    result.append(res)
                else:
                    raise ValueError('Один из списков в списке коротковат')
        else:
            raise ValueError('Один из списков коротковат')
        return Matrix(result)


matrix1 = Matrix([[1, 7, 4], [3, 5, 2], [2, 4, 2], [4, 6, 5]])
matrix2 = Matrix([[2, 3, 4], [3, 8, 9], [5, 2, 9], [3, 7, 4]])
print(matrix1)
print('-' * 10)
print(matrix2)
print('-' * 10)
print(matrix2 + matrix1)
