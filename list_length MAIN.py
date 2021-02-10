# Pg.86 - How to think cs
# ref to /home/sherms/Python files/How to think_exercises/listLength/README_listLength.txt
# ref to /home/sherms/Python files/How to think_exercises/listLength/tests.txt

think = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]]

def unpack_list(l):
    y = int(len(l)) # upper range limit
    index = 0
    new = []
    j = []
    for i in range(y):
        # print(l[i]) # prints each element from the list.
        new.append(l[i]) 
        index += # does not work as intended. It adds the think list to j four times.         
        j.append(new) # i need to unpack each element and add it as a new nested element to list j. i.e ['spam', 1] will become ['spam'] [1] in list j.
        
    # print(new, '- This is the new list.')
    print('APPENDED NEW LIST TO j ', j)
    
unpack_list(think)

