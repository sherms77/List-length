# https://stackabuse.com/python-get-number-of-elements-in-a-list/
# nested lists
# set recursion limit gives os error - ubuntu experienced an internal error

# list_f = [30, 0.9, [8, 56, 22, ["a", "b"]], [200, 3, [5, [89], 10]]]
think = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]]

def get_elements_of_nested_list(element):
    count = 0
    if isinstance(element, list):
        for each_element in element:
            count += get_elements_of_nested_list(each_element)
    else:
            count += 1
    return count

print("Total number of elements in the nested list: ", get_elements_of_nested_list(think))
# [in]: think
# [out]: Total number of elements in the nested list: 9 
# prints the aggregate of all elements in the list.