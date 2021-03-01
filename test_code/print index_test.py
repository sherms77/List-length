think = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]]
y = int(len(think)) # upper limit

print(think.index('spam!')) # need to use item not index no.
print(think.index('Brie')) # how to access nested element index?


'''
for i in range(y):
    print(think.index(i))
'''
