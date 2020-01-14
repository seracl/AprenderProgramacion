# 2D Array
"""
2D Array: Arrays within an array where the position of an data element is referred by two indices instead of one.
Represents a table with rows an dcolumns of data
"""
from array import *

## Definition
print('Defining a 2D array:'.upper())
empty_2da = [[],[],[]]
print (f"	- Empty dictionary: {empty_2da}")
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
print(f"	- Filled 2D array: {T}")


## Accessing Elements
print('Accessing Elements:'.upper())
print(f"	- T[0]   : {T[0]}")
print(f"	- T[1][2]: {T[1][2]}")
for r in T:
    for c in r:
        print(c,end = " ")
    print()

## Inserting Elements
print('Inserting Elements:'.upper())
T.insert(2, [0,5,11,13,6])
for r in T:
    for c in r:
        print(c,end = " ")
    print()

## Updating Elements
print('Updating Elements:'.upper())
T[2] = [11,9]
T[0][3] = 7
for r in T:
    for c in r:
        print(c,end = " ")
    print()

## Delete Elements
print('Delete Elements:'.upper())
del T[3]
for r in T:
    for c in r:
        print(c,end = " ")
    print()
