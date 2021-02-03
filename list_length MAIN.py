# Pg.86 - How to think cs
# ref to /home/sherms/Python files/How to think_exercises/listLength/README_listLength.txt
# ref to /home/sherms/Python files/How to think_exercises/listLength/tests.txt

think = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]]
e = ['spam!', ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3]] # list without standalone int 1

def unpack_list(l):
    y = int(len(l)) # upper range limit
    index = 0
    new = []
    j = []
    for i in range(y):
        # print(l[i]) # prints each element from the list.
        new.append(l[i]) # works but doesn't nest all the elements. Elements 0 and 1 are still unnested in new list.
        index +=1
        j.append(new)
        
    # print(new, '- This is the new list.')
    print('APPENDED NEW LIST TO j ', j)
    print(len(j))
unpack_list(think) # does not work correctly.

'''
def my_list(l):
    print(l)

my_list(think)
'''
