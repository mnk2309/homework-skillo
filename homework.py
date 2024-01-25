print("Problem 1")

a=6
b=2

print(a+b)
print(a-b)
print(a*b)
print (a/b)

print("Problem 2")

List_of_names_and_PINs = ("Angel Ivanov 9812316070",
                          "Ognyan Marinov 9304123256",
                          "Kristian Mehandzhiyski 9103142514",
                          "Bogdan Syarov 9001194578",
                          "Irina Barzakova 8009146594")

vowels = ["A", "O", "U", "E", "I"]

names_of_interest = {}
for index, record in enumerate(List_of_names_and_PINs):
    first_letter = record[0]
    if first_letter in vowels:
        names_of_interest[index] = record

print(names_of_interest)

print("Problem 3")


headers = ["x", "y", "x and y", "x or y", "not x", "not y"]

values = [(True, True), (True, False), (False, True), (False, False)]

print("|".join(headers))

for x, y in values:

    x_and_y = x and y
    x_or_y = x or y
    not_x = not x
    not_y = not y

    print(f"{x} | {y} | {x_and_y} | {x_or_y} | {not_x} | {not_y}")

print("Homework lecture 3: Work in progress...")





