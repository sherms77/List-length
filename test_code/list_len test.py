# https://stackabuse.com/python-get-number-of-elements-in-a-list/
# counts elements in a nested list

list_c = [20, 8.9, 'Hi', 0, 'word', 'name']

def get_num_of_elements(list):
    count = 0
    for element in list:
        count +=1
    return count

print('Number of elements in the list: ', get_num_of_elements(list_c))
