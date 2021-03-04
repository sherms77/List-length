think = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]]
new = []

def new_nested(x):
    y = int(len(x)) # upper limit

    for item in range(y):
          print(x[item])
          c = str(x[item]) # converts item to a string
          new.append(c)

    print('\nIs the list now string?', isinstance(new[1], str)) # checks if all elements in list are a string
    print('New list as a string', new)

    for idx, val in enumerate(new):
        sub_white = len(new[idx]) - new[idx].count(' ')
        
        print('\nThe len of element at index', idx, 'is:', sub_white)
        print('The len of value:', val, 'is:', sub_white)
     
new_nested(think)


    
