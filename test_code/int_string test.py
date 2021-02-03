# testing why len for string conversion returns wrong length
# https://stackoverflow.com/questions/2225038/determine-the-type-of-an-object

j = ['t', 'c', 'h', 'f']
n = [1, 2, 3, 4]
# len(str(n)) # no output
print("No. of elements in j:", len(j)) # expected output = 4 - correct output
print("No of elemets in n, int converted to str:", len(str(n))) # returns 9 - incorrect len: need to debug.
# 221220: debug does not tell me why len is 9 when you convert to str.
# 221220: amigos code fb group advised that when it converts to string it adds quotes and counts every character.
print("No. of elements in n, int not converted:", len(n))

'''
j = ['hi', [1, 2], ['me', 'myself'], [7]]

print(len(j[0])) # 2 - works
print(len(j[1])) # 2 - works

k = ['b', 2]
# print(len(k)) # works

x = ['j', 9, ['v', 'yo']]
# print(len(x))
# print(len(x[0])
print(len(x[1])) # error - int has no len
'''

