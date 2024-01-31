def sumElements(arr):
    result_1 = 0
    for element in arr:
        result_1 += element
    return result_1


resultSum = sumElements([1, 2, 3, 4])
print(resultSum)

print(sumElements([1, 2, 3, 4]))
print(sumElements([0]))
print(sumElements([]))
print(sumElements([-1, 1]))
