class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def start_car(self):
        print("Автомобиль заведен")
    def stop_car(self):
        print("Автомобиль заглушен")
    def set_color(self, newColor):
        self.color = newColor
    def set_type(self, newType):
        self.type = newType
    def set_clear(self, newYear):
        self.year = newYear
    def get_info(self):
        return print(self.color, self.type, self.year)
car1 = Car('red', 'jip', 2000)
car2 = Car('blue', 'jip', 2000)
car3 = Car('green', 'jip', 2000)
car4 = Car('red', 'minivan', 2015)
car5 = Car('blue', 'jip', 2000)
car4.get_info()