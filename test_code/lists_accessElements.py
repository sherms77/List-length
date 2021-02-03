# Pg. 85 - How to think like a cs
# loop variable index example

horsemen = ['war', 'famine', 'pestilence', 'death', 'resurrection']

i = 0
while i < 4:
    print(horsemen[i])
    i +=1 # i = i + 1 - this is in book. Used shorthand instead.

# when loop variable is 4, loop terminates.
# body of loop is only executed when i is 0, 1, 2 and 3.
# each time through the loop, the variable i is used as an index into the list.
# it prints the i-eth element.
# this pattern of computation is called a list traversal.

# Pg.86 example
x = 0
print('\nPg.86 example - uses len for upper bound of loop')
while x < len(horsemen):
    print(horsemen[x])
    x +=1

# uses len as upperbound for loop
# used x instead of i to differentiate
