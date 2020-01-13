# Array
"""
Arrays are the base of most algorithm implementations.
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

print('Array: '.upper())
numbers = [10,20,300,40.5,50,'hello']
print(f'Numbers is an array of size {numbers.__len__()}: {numbers}')

# Random indexing --> 0(1) get items if we know the index!!!
print(f'Element at index {numbers.index(numbers[4])} is {numbers[4]}')

numbers[-1] = 'Adam'
print(f'Element at index {numbers.index(numbers[-1])} is {numbers[-1]}')

print('Printing array elements independently:')
for num in numbers:
	print(f' - Element of array: {num}')

print('Printing array elements at their index:')
for i in range(len(numbers)):
	print(f' - Element at index {i}: {numbers[i]}')

# O(N) search running time
numbers[-1] = 25
maximum = numbers[4]
for num in numbers:
	if num > maximum:
		maximun = num

print(maximum)

# Multidimensional array
"""
Very important in mathematical computation (matrixes)
	- arrayName[row index][column index]
		 arrayName[->][┴]
	- Arrays can have as many dimensions as needed
			Array                  -> One dimensional array
			Multidimensional array -> Matrix
			Dynamic array 				 -> The size of the array change dynamically
			Applications           -> lookup tables/hastables, heaps
Advantages
	- It allows random access getItem(index)
	- Fast return values O(1)
	- Should be used when adding items multiple times and want to retrive items at given indexes 
Disadvantages
	- 
"""