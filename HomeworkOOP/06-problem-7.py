class Animal:
    def __init__(self, name, food):
        self.name = name
        self.food = food


class Dog(Animal):

    def __init__(self, name, food, habit):
        super().__init__(name, food)
        self.habit = str(habit)

    def __str__(self):
        return f'{self.name} eats {self.food} and {self.habit}.'


class Cat(Animal):
    def __init__(self, name, food, habit):
        super().__init__(name, food)
        self.habit = str(habit)

    def __str__(self):
        return f'{self.name} eats {self.food} and likes to {self.habit}.'


dog = Dog("Bengie", "bones", "go on long walks in the park")
cat = Cat("Snowball", "milk", "catch mice")

print(dog)
print(cat)
