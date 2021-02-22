import string

l = ['spam!', 1, [2,3], 'h', 4, [5,6]]
      
# unpacks list
def new_list_prod(r):
    z = int(len(r))
    index = 0
    v = string.ascii_letters

    print('\nNew list names.\nThe unpacked elements will be saved individually in these lists:')
    for letter in range(z):
        t = v[letter] # stores letter from v list in t variable
        print(t) # prints letters stored in t on each iteration
        t = [] # new lists names based on letters generated from ASCII list
    
    print('Unpacked elements:')
    for element in range(z):
        print(r[element])
        r[element]

        # PROBLEM WITH REPACKING - REFER TO LINKS 5 and 7 in notes.txt.
        print('\nRepacked elements:')
        t.append(r[element]) # this seems to work but its appending each element to the next new list. It needs to save one element per list.
        # need to use add to list not append?
        print(t) # prints values of each new list
    
new_list_prod(l)

'''
# saves individual lists as nested elements in aggregate list
def aggregate_list():
    pass 
'''

      
