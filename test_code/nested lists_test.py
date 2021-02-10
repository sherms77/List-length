# https://stackabuse.com/python-get-number-of-elements-in-a-list/
# nested lists

# list_f = [30, 0.9, [8, 56, 22, ["a", "b"]], [200, 3, [5, [89], 10]]]
# think = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]]
think =  ['spam', 'hello', 1, 2, 3, 4] # list with unnested elements

def get_elements_of_nested_list(element):
    count = 0
    if isinstance(element, list):
        for each_element in element:
            count += get_elements_of_nested_list(each_element) # recursive function call
    else:
            count += 1
    return count

print("Total number of elements in the nested list: ", get_elements_of_nested_list(think))

# in[think]: think = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]]
# out[think]: Total number of elements in the nested list: 9 
# prints the aggregate of all elements in the list.

# QUESTION: Can I use this to code to count the len of each element individually?
# Ie: in[len(think[0])]: think = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]] 
#     out[len(think[0])]: 5
#     in[len(think[2])]: think = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]] 
#     out[len(think[2])]: 3

# isinstance: Checks an object's data type. Eg: isinstance("hey", str). Out: True. It returns a boolean.
# isintance: The second argument can be a tuple. Eg: isinstance(["hey"], (str, int, list)) Out: True. One of the arguments in the tuple makes the first argument true.

# Flow of execution
# 1.Uses isinstance to set a condition of: execute the for loop if the argument is a list.
# 2.If it is, then the for loop loops inside the list and recursively calls the function until there are no nested lists left.
# 3.The body of the for loop increases the count by one for each individual element.
# 110221: DEBUGGING TO UNDERSTAND WHAT THE ELSE STATEMENT DOES. USING A LIST WITH UNNESTED ELEMENTS TO TEST IT.