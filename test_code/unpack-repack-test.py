# l = ['spam!', 1, [2,3]]
l = ['spam!', 1]
# l = ['spam!']

def repack(d):
    y = int(len(d))
    for i in range(y):
        print(d[i])
        n = []
        n.append(d[i]) #stores the index val
        # print(n)
        
    print('Full list:',(n)) # only adding last item as index
    # full list needs to be printed here.
        
repack(l)

# DATE: 180221

# 1.if i store each unpacked item in it's own list
# 2.then append those lists to a new list
# 3.it will give me a list with nested elements

# MIGHT HAVE TO WRITE A LOOP TO CREATE A NEW LIST FOR EACH UNPACKED ELEMENT.
# NOT AN EFFICIENT SOLUTION BUT WILL LET ME SEE OPERATION.

# REFER TO SCREENSHOT IN PICTURES FOLDER.

# LIST COMPREHENSION MIGHT BE A CLEANER WAY TO DO IT?

# Note: after I get the repacking to work, I will need to use len of new list as upper range limit.
