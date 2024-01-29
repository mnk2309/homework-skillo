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

print("Homework lecture 3:")
print("Problem 0")

number = int(input("Write a number: "))

if number %2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')

print("Problem 1")
Sum = int()
for digit in range(1, 101):
    if digit %2 == 0:
        Sum += digit
print('Sum', Sum)

print("Problem 2")

answer = 22
while True:
    userAnswer = int(input("How much is 5 + 17: "))
    if userAnswer == answer:
        print("Coreect!")
        break
    else:
        print("Incorrect! Try again")

print("Problem 3")

for i in range(1, 1001):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print("Problem 4")

import random

targetNumber = random.randint(1, 100)

while True:
    guess = int(input("What is the correct number between 1 and 100? : "))

    if guess == targetNumber:
        print("Correct! You win!")
        break
    elif guess < targetNumber:
        print("Too low! Try again.")
    elif guess > targetNumber:
        print("Too high! Try again.")

print("Problem 5")

import random

while True:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    operator = random.choice(['+', '-'])

    if operator == "+":
        corAns = num1 + num2
    elif operator == "-":
        corAns = num1 - num2

    userAnswer = int(input(f"How much is {num1} {operator} {num2} equal to? "))

    if userAnswer == corAns:
        print("Correct!")
        break
    else:
        print("Incorrect! Try again")


print("Problem 6")

integer = int(input("Put your number: "))

print(f'Multiplication table for {integer}')
for x in range(1, 11):
    result =integer * x
    print(f"{integer} * {x} = {result}")

print("Problem 8")

n = int(input("Declare number of rows: "))
for a in range(1, n + 1):
    for b in range(1, a + 1):
        print(b, end="")
    print()

