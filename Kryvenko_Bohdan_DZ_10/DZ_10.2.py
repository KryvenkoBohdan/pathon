'''
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определённое название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке
знания. Реализовать абстрактные классы для основных классов проекта и проверить работу
декоратора @property.
'''
from abc import ABC, abstractmethod


class Dress(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def fabric_for_dress(self):
        pass


class Coat(Dress):
    @property
    def fabric_for_dress(self):
        return round(float(self.param / 6.5 + 0.5), 2)


class Costume(Dress):
    # @property        это я для себя чтобы понять и запомнить разницу
    def fabric_for_dress(self):
        return round(float(2 * self.param + 0.3), 2)


coat = Coat(22)
costume = Costume(22)
print(coat.fabric_for_dress)
print(costume.fabric_for_dress())
