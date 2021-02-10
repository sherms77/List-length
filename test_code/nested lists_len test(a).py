# https://stackabuse.com/python-get-number-of-elements-in-a-list/
# counts the number of elements in all lists within the list

list_e = [[90, 4, 12, 2], [], [34, 45, 2], [9, 4], "char", [7, 3, 19]]

# number_of_elements = len(list_e)
# print("Number of elements in the list of lists: ", number_of_elements)

number_of_elements = sum([len(element) for element in list_e]) # list comprehension
print("Number of elements in the list of lists: ", number_of_elements)

def get_all_elements_in_list_of_lists(list):
    count = 0
    for element in list_e:
        count += len(element)
    return count

print("Total number of elements in the list of lists: ", get_all_elements_in_list_of_lists(list_e))
