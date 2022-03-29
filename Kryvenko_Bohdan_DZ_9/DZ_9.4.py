'''
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction),которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(f'Автомобиль {self.name}, цвет {self.color} поехал')

    def stop(self):
        return print(f'Автомобиль {self.name} остановился')

    def turn(self, derection):
        return print(f'Автомобиль {self.name} повернул на {derection}')

    def show_speed(self):
        return print(f'Скорость автомобиля {self.name} составляет: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print('Привышение скорости!!!')
        return print(f'Скорость автомобиля {self.name} составляет: {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print('Привышение скорости!!!')
        return print(f'Скорость автомобиля {self.name} составляет: {self.speed} км/ч')


class Police(Car):
    pass


t_c = TownCar(90, 'зеленый', 'Форд', False)
t_c.go()
t_c.stop()
t_c.turn('право')
t_c.show_speed()
print(50 * '*')
s_c = SportCar(120, 'красный', 'Ферари', False)
s_c.go()
s_c.stop()
s_c.turn('лево')
s_c.show_speed()
print(50 * '*')
w_c = WorkCar(90, 'ржавый', 'Камаз', False)
w_c.go()
w_c.stop()
w_c.turn('лево')
w_c.show_speed()
print(50 * '*')
p_c = Police(160, 'синий', 'Шкода', True)
p_c.go()
p_c.stop()
p_c.turn('лево')
p_c.show_speed()