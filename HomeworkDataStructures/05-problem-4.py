# Write a function that takes a list and returns the sum of all even numbers in the list.

def totalSum(numberslist):
    grandTotal = 0

    for number in numberslist:
        if number % 2 == 0:
            grandTotal += number

    return grandTotal


numbers = list(range(1, 101))
result = totalSum(numbers)
print(result)
