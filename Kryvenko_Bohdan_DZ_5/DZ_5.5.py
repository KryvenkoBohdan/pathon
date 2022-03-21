'''
5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
'''
from time import perf_counter
from sys import getsizeof

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
start = perf_counter()
for i in src:
    if src.count(i) == 1:
        result.append(i)
print(f'{result} скорость срабатывания: {perf_counter() - start:.6f}, размер: {getsizeof(result)}')

start2 = perf_counter()
result2 = [i for i in src if src.count(i) == 1]
print(f'{result2} скорость срабатывания: {perf_counter() - start2:.6f}, размер: {getsizeof(result2)}')

unique_nums = set()
tmp = set()
start3 = perf_counter()
for num in src:
    if num not in tmp:
        unique_nums.add(num)
    else:
        unique_nums.discard(num)
    tmp.add(num)
result3 = [num for num in src if num in unique_nums]

print(f'{unique_nums} скорость срабатывания: {perf_counter() - start3:.6f}, размер: {getsizeof(unique_nums)}')
print(f'{result3} скорость срабатывания: {perf_counter() - start3:.6f}, размер: {getsizeof(result3)}')
