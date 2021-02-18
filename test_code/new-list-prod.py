# loops to create new letter that can be used to a new list for each unpacked element from root list.

import string
# string.ascii_letters - upper and lower case letters
# string.ascii_lowercase - lower case letters only
# string.ascii_uppercase - upper case letters only

l = ['spam!', 1]

def new_list_prod(r):
    z = int(len(r))
    index = 0
    v = string.ascii_letters
    m = []
    for j in v: # for j in range(z):
        # print(j)
        m.append(j)

    print(m)

        # how do I only print a letters within range z?
        
new_list_prod(l)
            
            
