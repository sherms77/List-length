think = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2 ,3, 4]]
y = int(len(think)) # upper limit

# print(think.index('spam!')) # need to use item not index no.
# print(think.index('Brie')) # how to access nested element index?
# print(think[2][0])
# print(think.index(['Brie', 'Roquefort', 'Pol le Veq'])) # works OUT[]: 2
print(think.index(['spam!'])) # this does not work bc 'spam!' is not nested, returns value error.

'''
for e in range(y):
    print(think[e])
# this loop iterates over the list and prints each element.
'''

'''
for i in range(y):
    print(think.index(i))
'''