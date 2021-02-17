# this function will not work if the list has an unnested integer in it.

t = ['spam!', ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]]
# t = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq']] # will not work, has an unnested integer.

def list_length(l):
    i = 0 # index
    y = int(len(l)) # upper range limit
    print('Here is your list:', (l))
    print('There is a total of', len(l),'elements in the list.')
    print('The length of each element in the list is:')
    for j in range (y):
        print('-Element',[j],'=',len(l[j]))
        i = i + 1

list_length(t)