def min_or_max(tuple_of_int):
    maxi_value = mini_value = tuple_of_int[0]

    for number in tuple_of_int[1:]:
        if number > maxi_value:
            maxi_value = number
        elif number < mini_value:
            mini_value = number
    return maxi_value, mini_value


myTuple = (1, 2, 43, 54, 90, 37, 12)
maxi_value, mini_value = min_or_max(myTuple)

print("Minimum Value:", mini_value)
print("Maximum Value:", maxi_value)
