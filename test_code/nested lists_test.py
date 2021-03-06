# https://stackabuse.com/python-get-number-of-elements-in-a-list/
# nested lists

think =  ['spam', 'hello', 1, 2, 3, 4] # list with unnested elements

# list_f = [30, 0.9, [8, 56, 22, ["a", "b"]], [200, 3, [5, [89], 10]]]
# think = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]]
# think = {1:'hello', 2: 'goodbye', 3: 'hi', 4: 'bye'} # dict not a list to test else statement - else statement counts the entire dict as one element. does not count elements in it.
# think = {'a':{1: 'hello', 2: 'goodbye', 3: 'hi', 4: 'bye',}, 'b':{5: 'bonjour', 6: 'koniciwa', 7: 'aloha'}} # nested dicts to test else statement - else statement still counts nested dicts as one element. just counts the whole outer dictionary.
# think = ('hi', 'hello', 'bye', 'goodbye') # tuple to test the else statement.
# think = ('hi', 'hello', 'bye', 'goodbye', ('bonjour', 'aloha')) # nested tuple to test else statement - else statement only counts it as one. does not count inner elements.

def get_elements_of_nested_list(element):
    count = 0
    if isinstance(element, list):
        for each_element in element:
            count += get_elements_of_nested_list(each_element) # recursive function call
    else:
            count += 1
    return count

print("Total number of elements in the nested list: ", get_elements_of_nested_list(think))

# Flow of execution
# 1.Uses isinstance to set a condition of: execute the for loop if the argument is a list.
# 2.If it is, then the for loop loops inside the list and recursively calls the function until there are no nested lists left.
# 3.The body of the for loop increases the count by one for each individual element, unless its an empty list.
# 4.If not a list, the else statement is executed. The else statement does not count all individual elelments in its structure. Ie: nested tuple, will only count the entire tuple.
# 5.Returns count when finished.

# in[think]: think = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]]
# out[think]: Total number of elements in the nested list: 9 
# prints the aggregate of all elements in the list.

# QUESTION: Can I use this code to count the len of each element individually?
# Ie: in[len(think[0])]: think = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]] 
#     out[len(think[0])]: 5
#     in[len(think[2])]: think = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]] 
#     out[len(think[2])]: 3

'''
How isinstance works: 
    1.Checks an object's data type. Eg: isinstance("hey", str). Out: True. It returns a boolean.
    2.The second argument can be a tuple. Eg: isinstance(["hey"], (str, int, list)) Out: True. One of the arguments in the tuple makes the first argument true.
'''


