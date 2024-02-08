# Problem 9:
# Create a class called "Employee" that has attributes name, start_date, PIN, phone, address,
# manager_name, department. Decide their access specifiers. Implement methods to calculate
# employee tenure, and business card info representation.
import datetime


class Employee:
    def __init__(self, name, pin, phone, manager_name, department, start_date):
        self.name = name
        self.pin = pin
        self.phone = phone
        self.manager_name = manager_name
        self.department = department
        self.start_date = start_date

    def __str__(self):
        return (f'{self.name}\n'
                f'{self.department}\n'
                f'{self.phone}\n')

    def calculate_tenure(self):
        present_date = datetime.date.today()
        tenure = present_date - self.start_date
        return f'{tenure.days} days'


start_date = datetime.date(2001, 4, 30)
adam = Employee("Adam Sandler", 2580, "+359888888899", "Ivan Ivanov", "Marketing", start_date)

print(adam)
print(f'Tenure:', adam.calculate_tenure())


start_date_lilly = datetime.date(2011, 8, 12)
lilly = Employee("Lilly Knowles", 6598, "+359899785614", "Stoyan Panev", "R&D", start_date_lilly)

print(lilly)
print(f'Tenure:', lilly.calculate_tenure())
