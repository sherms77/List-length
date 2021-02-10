# pasted code from: nested lists section in https://stackabuse.com/python-get-number-of-elements-in-a-list/
# code works
# my code didn't when I typed it out
# my indentations were incorrect
# corrected in nested_lists.py

list_f = [30, 0.9, [8, 56, 22, ["a", "hello"]], [200, 3, [5, [89], 10]]]

def get_elements_of_nested_list(element):
    count = 0
    if isinstance(element, list):
        for each_element in element:
            count += get_elements_of_nested_list(each_element)
    else:
        count += 1
    return count

print("Total number of elements in the nested list: ", get_elements_of_nested_list(list_f))
