# Lists
"""
The most versatile datatype in Python 
Can be written as a list of comma-separated values (items) between square brackets.
Items in a list need not be of the same type
Similar to string indices, list indices start at 0, and lists can be sliced, concatenated
"""
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

## Accessing Elements
print('Accessing Elements:'.upper())
print (f"	- list1[0]: {list1[0]}")
print(f"	- list2[1:5]: {list2[1:5]}")

## Updating Elements
print('Updating Elements:'.upper())
print(f"	- Original list: {list1}")
list1[-1]=2001
print(f"	- list2[-1] from 2000 to: {list1[-1]}")
list1[1]='physics'
print(f"	- list2[1] from chemistry to: {list1[1]}")
print(f"	- Updated list: {list1}")

## Delete Elements
print ('Delete Elements:'.upper())
print (f"	- Original list: {list1}")
del list1[-1]
print (f"	- New list: {list1}")

## Basic Operations
print ('Basic List Operations:'.upper())
print (f"	- Length:         {len(list1)}")
print (f"	- Concatenation:  {list1 + [4, 5, 6]}")
print (f"	- Repetition:     {['Hi!'] * 4}")
print (f"	- Membership:     {3 in list2}")
print (f"	- Iteration:      {'for x in [1, 2, 3]: print x'}")