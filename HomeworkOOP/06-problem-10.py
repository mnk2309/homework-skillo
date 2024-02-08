from abc import ABC


class Employee(ABC):
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        self._message = []

    def send_message(self, message):
        self._message.append(message)

    def get_message(self):
        return self._message


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def send_message(self, message):
        super().send_message(message)


class Team:
    def __init__(self, manager, members):
        self.manager = manager
        self._members = members

    def send_message_to_team(self, message):
        for member in [self.manager] + self._members:
            member.send_message(message)


manager = Manager("Jimmy Joel", 5000, "Sales")

employee1 = Employee("Robbert Hurts", 1000)
employee2 = Employee("Tina Thunder", 1100)

team = Team(manager, [employee1, employee2])

team.send_message_to_team("Corporate meeting at 1:00 PM sharp!")
print(employee1.get_message())
print(employee2.get_message())
print(manager.get_message())

