# Pg.86 - How to think cs
# ref to /home/sherms/Python files/How to think_exercises/listLength/README_listLength.txt

think = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]]
new = []

def list_length(x):
    y = int(len(x)) # upper limit

    for item in range(y):
          # print(x[item])
          c = str(x[item]) # converts item to a string
          # print('Is the list now a string?\n', isinstance(c, str)) # checks if item is a string
          new.append(c)

    # print('Is the list now a string?', isinstance(new, str)) # checks if item is a string
    # out [isintance(new, str)]: False - Unsure why? 
    # above does not work bc its checking the entire list and not the elements inside.
          
    # new_sub = int(len(new))
    k = int(len(new)) - new.count(' ') # new upper limit for new list with whitespaces

    # CREATE FOR LOOP TO ITERATE OVER INDEX NUMBERS
    # THEN PUT ITERABLE INDEX NUMBERS IN PRINT STATEMENT FOR LEN OF EACH ELEMENT IN RELEVANT INDEX

    for element in range(k):
        sub_white = len(new[element]) - new[element].count(' ')
        print('The length of element in index', new[element], 'is', sub_white)

list_length(think)