class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'yellow', 'violet', 'orange', 'brown', 'gray', 'black', 'white']

    def __init__(self, owner, model, color, power):
        self.owner = str(owner)
        self.__model = str(model)
        self.__color = str(color)
        self.__engine_power = int(power)

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def set_color(self, color):
        if color.lower() in self._Vehicle__COLOR_VARIANTS:
            self._Vehicle__color = color
        else:
            print(f'Нельзя сменить цвет на {color}')


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
