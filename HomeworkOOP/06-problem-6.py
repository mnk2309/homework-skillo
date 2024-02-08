class Book:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def __len__(self):
        return self.length

    def __str__(self):
        return f'{self.name}, {self.length}'


book1 = Book("Lord of the Rings", 1300)
book2 = Book("Count of Monte Cristo", 1200)

print(book1)
print(book2)
