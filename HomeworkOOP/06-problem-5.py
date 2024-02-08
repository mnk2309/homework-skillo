
class Vehicle:

    def start_engine(self):
        pass

    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def start_engine(self):
        return f'{self.name} goes Brum-brum'


class Bicycle(Vehicle):
    def start_engine(self):
        return f'{self.name} goes Ring-ring'


car = Car("Subaru")
bicycle = Bicycle("Peugeot")

print(car.start_engine())
print(bicycle.start_engine())
