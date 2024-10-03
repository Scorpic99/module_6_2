class Vehicle:
    owner = ''
    __model = ''
    __engine_power = 0
    __color = ''
    __COLOR_VARIANTS = ('RED', 'GREEN', 'YELLOW', 'BLUE', 'GRAY')

    def __init__(self, model, color, engine_power):
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def print_info(self):
        print(f'Модель: {self.get_model()}\nМощность двигателя: {self.get_horsepower()}\nЦвет: {self.get_color()}')
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        flag = False
        for i in self.__COLOR_VARIANTS:
            if i.lower() == new_color.lower():
                flag = True
                break
            else:
                flag = False
        if flag:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        super().__init__(model, color, engine_power)

    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('Gray')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()