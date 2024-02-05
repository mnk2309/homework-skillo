set1 = {1, 2, "David", "Alice", 5, 6}
set2 = {1, "Alice", 6, "Charlie"}

set3 = set1.intersection(set2)
print(set3)


def is_sub_set(set1, set2):
    return set1.issubset(set2)


result = is_sub_set(set1, set2)
if result:
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")

