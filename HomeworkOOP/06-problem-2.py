# Create a class "Student" with private attributes for name and age. Implement getter and setter
# methods for these attributes. Demonstrate their usage.


class Student:
    def __init__(self, name, age):
        self.__private_name = name
        self.__private_age = age

    def set_private_name(self, value: str):
        self.__private_name = value

    def set_private_age(self, value: int):
        self.__private_age = value

    def get_private_name(self):
        return self.__private_name

    def get_private_age(self):
        return self.__private_age

    def __str__(self):
        return f'{self.__private_name}, {self.__private_age}'


John = Student("John", 28)
Merry = Student("Merry", 19)

print(John.get_private_name(), John.get_private_age())


print(Merry.get_private_name(), Merry.get_private_age())



