this_list = ["apple", "tomato", "pineapple", "apple", "cherry", "watermelon", "tomato"]


def remove_duplicates(my_set):
    unique_items = set(my_set)
    return list(unique_items)


final_list = remove_duplicates(this_list)
print(final_list)