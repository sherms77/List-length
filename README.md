# Think CS exercise - Pg.86
STATUS: Active.

# PROBLEM
1.As an exercise, write a loop that traverses the previous list and prints the length of each element. 2.What happens if you send an integer to len?

# ANSWER TO PROBLEM 2
If you send an integer to a len (with mixed elements) and you try to get its len, you get an error. However, you get the len of a list that only has integers in it or, if there is nested list with only intergers in it you will get the len of the nested list.

# FILES
list_lengthMAIN.py - MAIN
notes.txt
README.md
tests(folder):
	int_stingtest.py
	list_lentest.ppy
	lists.py
	lists_accessElements.py
	list_settest.py
