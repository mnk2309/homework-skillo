# Create a class "Person" with a special method "__str__" to provide a string representation.
# Instantiate an object of this class and print it.

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


    def __str__(self):
        return f"{self.name}, {self.email}"


john = Person("John", "john.doe@mail.com")

print(john)



