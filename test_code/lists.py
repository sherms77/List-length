# Pg. 83 - 85 - How to think like a cs
# examples

# no variables assigned
# works in shell
[10, 20, 30, 40]
['spam', 'bungee', 'swallow']
['hello', 2.0, 5, [10, 20]]

list_range = list(range(10)) # this also works as an equivalent to range(5) in Python 2
print(list_range, '\n')

for i in range(1,6):
    print(i, end = ' ')
print('\n')

for x in range(10):
    print(x, end = ' ')
print('\n')

for j in range(1, 10, 2):
    print(j, end = ' ')
print('\n')

vocabulary = ['amelirate', 'castigate', 'defenestrate']
numbers = [17, 123]
empty = []

print(vocabulary, numbers, empty)

print(numbers[0])
numbers[1] = 5
print(numbers)
numbers[3-2]

# numbers[1.0] # error
# numbers[2] = 5 # error

numbers[-1]
numbers[-2]

# numbers[-3] # error


