# loops to create new letter that can be used to a new list for each unpacked element from root list.

import string
# string.ascii_letters - upper and lower case letters
# string.ascii_lowercase - lower case letters only
# string.ascii_uppercase - upper case letters only

l = ['spam!', 1, [2,3], 'h', 4, [5,6]]

def new_list_prod(r):
    z = int(len(r))
    index = 0
    v = string.ascii_letters
        
    print('Unpacked elements:')
    for element in range(z):
        print(r[element])
        r[element]
    
    # produces new list names for each unpacked element
    print('\nElements repacked:')
    for letter in range(z):
        # print(v[letter]) # prints an ascii letter from list in v

        t = v[letter] # stores letter from v list in t variable
        print(t) # prints letters stored in t on each iteration
        t = []
        t.append(r[element]) # appends values from r list to new lists - does not work, only appends the last element?
        print(t) # prints values of each new list
        
new_list_prod(l)
            
            
