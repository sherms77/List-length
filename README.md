# Think CS exercise - Pg.86

# Status
Finsished - 4 March 2021.

# Problem
1.As an exercise, write a loop that traverses the previous list and prints the length of each element. 2.What happens if you send an integer to len?

# Solution | Problem 1
1.Converted each item in the list to a string.
2.Saved converted items to a new list.
3.Use isinstance function to check if new list is a string.
4.Removed whitespace from each element.
5.Ran len() on each element in new list.
6.Used enumerate function to show index of each element and its length.

# Solution | Problem 2
If you send an integer to the len() function, it does not work. It returns an error, you cannot use the len() function on an integer. However, if you use len() on a nested list with integers in it, it will work - it returns the len of the nested list.

# Files
list_length MAIN(3).py - MAIN
note.txt
README.md
test_code(folder): test files
archive(folder): old files
# Notes
120221: Do not move this repo to Python challenges. Do not want to disrupt existing repo.
