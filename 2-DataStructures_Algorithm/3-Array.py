# Array
"""
Array is a container which can hold a fix number of items and these items should be of the same type.
Most of the data structures make and algorithms use of arrays to implement their algorithms.
Arrays are structures composed by:
	- Element: Each item stored in an array is called an element.
	- Index: Each location of an element in an array has a numerical index, which is used to identify the element.

Array Representation
	Arrays can be declared in various ways in different languages:
		In C: dataType arrayName[size] = {elements of the array}
					int array[10] = {10,20,25,55,110}
		In Python: array = ['hello, 10, 23.5, "Momo"]
	The array index start at 0 to n-1: 
		At array size 10, index goes from 0 to 9
	Because of the indexes random access is possible

Basic operations
	- Traverse: print the array elements one by one.
	- Adding: Add an element to array at O(1)
	- Insertion: Adds an element at the given index O(N).
	- Deletion: Deletes an element at the given index.
	- Search: Searches an element using the given index or by the value.
	- Update: Updates an element at the given index.
"""
from array import *

## Array declaration
print('Array declaration:'.upper())
print('arrayName = array(typecode, [Initializers])')
array_num = array('i', [1,3,5,7,9,10,15])
print(f' - Item Size: {array_num.itemsize}')

## Printing array elements
print('Printing array elements:'.upper())
for i in range(len(array_num)):
 print(f' - Element at index {i}: {array_num[i]}')

## Accessing array elements
print('Accessing array elements:'.upper())
print(f' - Element {array_num.index(array_num[-1])}: {array_num[-1]}')

## Inserting array elements
print('Inserting array elements:'.upper())
array_num.insert(2,60)
print(f' - New array: {array_num}')

## Deleting array elements
print('Deleting array elements:'.upper())
array_num.remove(60)
print(f' - New array: {array_num}')

## Searching array elements
print('Searching array elements:'.upper())
print(f' - New array: {array_num.index(15)}')

## Updating array elements
print('Updating array elements:'.upper())
array_num[3] = 110
print(f' - New array: {array_num}')