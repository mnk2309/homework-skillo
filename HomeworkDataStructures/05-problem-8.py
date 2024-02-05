def hash_1(input_list):
    str_list = [str(element) for element in input_list]
    joined_string = ''.join(str_list)
    hash_value = hash(joined_string)
    return hash_value


list1 = [1, 2, 3, 'apple']
list2 = [1, 'apple', 3, 2]

hash1 = hash_1(list1)
hash2 = hash_1(list2)

print(f"Hash value for list1: {hash1}")
print(f"Hash value for list2: {hash2}")
