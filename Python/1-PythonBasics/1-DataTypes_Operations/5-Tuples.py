### Python Touples
'''
A tuple is an ordered inmutable sequence of objects, similar to the list, but enclosed within parentheses instead. 
A tuple consists of a number of any data type and separated by commas. 
Touples cannot be updated, can be thought of as read-only lists.
'''
touple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytouple = (123, 'john')

print('Touples:'.upper())
print ('Accessing Values in Strings:')
print ("- Prints complete touple:                       {}".format(touple))
print ("- Prints first element of the touple:           {}".format(touple[0]))
print ("- Prints elements starting from 2nd till 3rd :  {}".format(touple[1:3]))
print ("- Prints elements starting from 3rd element:    {}".format(touple[2:]))
print ('Other:')
print ("- Prints touple two times:                      {}".format(tinytouple * 2))
print ("- Prints concatenated touples:                  {}".format(touple + tinytouple))

'''Touples vs lists: This would work with lists but not with inmutable touples'''
#touple[2] = 1000
#print(touple)               # Invalid syntax with tuple
print('\n') 

## Basic Operations
'''
- Length        | len(touple)                  | result: 4
- Concatenation | touple + tinytouple          | result: ('abcd', 786 , 2.23, 'john', 70.2, 123, 'john')
- Repetition    | ('Hi!') * 4                  | result: ('Hi!', 'Hi!', 'Hi!', 'Hi!')
- Membership    | 'jhon' in lista              | result: True
- Iteration     | for x in (1, 2, 3): print x, | result: 1 2 3
'''

## Indexing, Slicing, and Matrixes
'''
L = ('spam', 'Spam', 'SPAM!')
Touple[start:stop:count]
- Offsets start at zero          | L[2]  | result: SPAM!
- Negative: count from the right | L[-2] | result: Spam
- Slicing fetches sections       | L[1:] | result: ('Spam', 'SPAM!')
'''

## Built-in List Functions 
'''
- cmp(tuple1, tuple2)  | Compares elements of both tuples.
- len(tuple)           | Gives the total length of the tuple.
- max(tuple)           | Returns item from the tuple with max value.
- min(tuple)           | Returns item from the tuple with min value.
- tuple(list)          | Converts a list into tuple.
'''

## Tuple unpacking 
'''
Python Tuples In python tuples are used to sore immutable object. 
Python Tuples are very similar to lists except to some situations. 
Python tuples are immutable means that they can not be modified in whole program.

Packing and Unpacking a Tuple : 
In Python there is a very powerful tuple assignment feature that 
assigns right hand side of values into left hand side. 
In other way it is called unpacking of a tuple of values into a variable. 
In packing, we put values into a new tuple while in unpacking we extract those values 
into a single variable.
'''

### Tuple Unpacking
#### Example 1
a = ("MNNIT Allahabad", 5000, "Engineering") # Packing values into a variable
(college, student, type_ofcollege) = a       # Unpacking values of a variable
 
print ('Tuple unpacking example 1:')
print(college) 
print(student) 
print(type_ofcollege)

#### Example 2
x, *y, z = (10, "Geeks ", " for ", "Geeks ", 50)  
	# first and last will be assigned to x and z, rest to y

print ('Tuple unpacking example 2a:')
print(x) 
print(y) 
print(z)

x, y, *z = (10, "Geeks ", " for ", "Geeks ", 50)  
	# first and second will be assigned to x and y, rest to z

print ('Tuple unpacking example 2b:')
print(x) 
print(y) 
print(z)

#### Example 3
mylist = [(1,2), (3,4),(5,6),(7,8)]

print ('Tuple unpacking example 3:')
print('Len of mylist is {}'.format(len(mylist))) 
print('Items on the list without unpacking'.capitalize())
for item in mylist:
    print('- Item : {}'.format(item))
print('Items on the list with unpacking'.capitalize())
for (a,b) in mylist:
    print('- Item a: {}'.format(a))
    print('- Item b: {}'.format(b))