# Pg.86 - How to think cs
# ref to /home/sherms/Python files/How to think_exercises/listLength/README_listLength.txt
# ref to /home/sherms/Python files/How to think_exercises/listLength/tests.txt

think = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]]

# running len on the unnested int element of 1 is the problem. len does not work on it in this format.
# 040221: READING THROUGH LINK 2 - LIST COMPREHENSIONS

def unpack_list(l):
    y = int(len(l)) # upper range limit
    index = 0
    new = []
    j = []
    for i in range(y):
        # print(l[i]) # prints each element from the list.
        new.append(l[i]) 
        index += # does now work as intended. It adds the think list to j four times.         
        j.append(new) # i need to unpack each element and add it as a new nested element to list j. i.e ['spam', 1] will become ['spam'] [1] in list j.
        
    # print(new, '- This is the new list.')
    print('APPENDED NEW LIST TO j ', j)

    # 030221: UPTO HERE
    # print(len(j[i])) # this didn't work. need to run len function on it and count nested elements.

unpack_list(think)

