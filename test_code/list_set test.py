# https://stackabuse.com/python-get-number-of-elements-in-a-list/
# counts the number of unique elements in the set

list_d = [100, 3, 100, "c", 100, 7.9,"c", 15]

# number_of_elements = len(list_d)
number_of_unique_elements = len(set(list_d))

# print("Number of elements in the list: ", number_of_elements)
print("Number of unique elements in the list: ", number_of_unique_elements)
