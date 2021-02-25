# append nested elements in a list

# WRAP LEN() IN A FOR LOOP

my_list = ['spam!', 1, [3,2], [4]]
new = []

def new_nested(x):
    y = int(len(x)) # upper limit

    for item in range(y):
          print(x[item])
          c = str(x[item]) # converts item to a string
          # print(c)

          # print(isinstance(c, str)) # checks if item is a string

          new.append(c)

    print(new,'\n') # works
    # print(new[0]) # works
    print(new[1]) # works
    print(new[2]) # works

    print('Is the list a string?', isinstance(new[1], str)) # checks if all elements in list are a string
    print('New list as a string', new)

    # WRAP LEN() IN A FOR LOOP
    print('\nLen for index [0] is', len(new[0]))
    print('Len for index [1] is', len(new[1]))
    print('Len for index [2] is', len(new[2])) # its counting the whitespace to give 6 characters
    print('Len for index [3] is', len(new[3])) 

    # 250221: Subtract the number of blank spaces from list - https://stackoverflow.com/questions/19669001/using-len-for-text-but-discarding-spaces-in-the-count
    
    # WRAP IN A FOR LOOP
         
new_nested(my_list)


    
