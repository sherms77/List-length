# https://stackabuse.com/python-get-number-of-elements-in-a-list/
# list comprehension

list_e = [[90, 4, 12, 2], [], [34, 45, 2], [9,4], "char", [7, 3, 19]]
num_of_elements = sum([len(element) for element in list_e])
print(num_of_elements)

# flow of execution
# 1.creates a new list containing the lengths of all the elements in list_e.
# 2.calls the sum function, using the new list as a paramater.
# 3.the sum function adds the lengths of all the elements together.


