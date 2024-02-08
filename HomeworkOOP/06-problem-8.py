class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_private_name(self):
        return self.__name

    def set_private_name(self, value: str):
        self.__name = value

    def get_private_salary(self):
        return self.__salary

    def set_private_salary(self, value: float):
        self.__salary = value

    def __str__(self):
        return f'{self.__name}, {self.__salary}'


class Manager(Employee):
    def __init__(self, name, department, salary):
        super().__init__(name, salary)
        self.department = department

    def get_department(self):
        return self.department

    def set_department(self, value: str):
        self.department = value


john = Manager("John Malkovich", "Marketing", 20000)
adam = Employee("Adam Sotkov", 2000)

print(john, john.get_department())
print(adam)
