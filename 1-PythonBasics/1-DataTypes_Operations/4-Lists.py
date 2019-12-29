# Python Lists
'''
Most versatile of Python's compound data types
Ordered sequence of objects, who's items are separated by commas and enclosed within square brackets ([]).
At to some extent similar to arrays in C, with the difference that that its items can belong to any data type 
Indexing, subsetting and slicing can be performed with the operators operator ([ ] or [:] or [::] ).
    Indexing start at 0 in the beginning and -1 at the end of the string
    The plus (+) sign is the concatenation operator and the asterisk (*) is the repetition operator.
'''

lista = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print ('Lists:'.upper())
print ('Accessing List Values:')
print ("- Prints complete list:                       %s" % (lista))
print ("- Prints first character of the string:       {}".format(lista[0]))
print (f"- Prints elements starting from 2nd till 3rd: {lista[1:3]} of type {type(lista[1:3])}")
print (f"Prints elements starting from 3rd element:    {lista[2:]}")
print ('Updating Lists:')
print ("- Prints list two times:                     ", tinylist * 2)    
print ("- Prints concatenated lists:                 ", lista + tinylist) 
print ('\t') 

## Basic Operations
'''
- Length        | len(lista)                   | result: 4
- Concatenation | lista + tinylist             | result: [ 'abcd', 786 , 2.23, 'john', 70.2, 123, 'john' ]
- Repetition    | ['Hi!'] * 4                  | result: ['Hi!', 'Hi!', 'Hi!', 'Hi!']
- Membership    | 'jhon' in lista              | result: True
- Iteration     | for x in [1, 2, 3]: print x, | result: 1 2 3
'''

## Indexing, Slicing, and Matrixes
'''
L = ['spam', 'Spam', 'SPAM!']        
- Offsets start at zero          | L[2]  | result: SPAM!
- Negative: count from the right | L[-2] | result: Spam
- Slicing fetches sections       | L[1:] | result: ['Spam', 'SPAM!']
'''

## Built-in List Functions & Methods
'''
Functions:
- cmp(list1, list2) | Compares elements of both lists.
- len(list)         | Gives the total length of the list.
- max(list)         | Returns item from the list with max value.
- min(list)         | Returns item from the list with min value.
- list(tup)         | Converts a tuple into list.

Methods
- list.append(obj)        | Appends object obj to list 
- list.count(obj)         | Returns count of how many times obj occurs in list
- list.extend(seq)        | Appends the contents of seq to list
- list.index(obj)         | Returns the lowest index in list that obj appears
- list.insert(index, obj) | Inserts object obj into list at offset index
- list.pop(obj=list[-1])  | Removes and returns last object or obj from list
- list.remove(obj)        | Removes object obj from list
- list.reverse()          | Reverses objects of list in place
- list.sort([func])       | Sorts objects of list, use compare func if give
'''

## List comperhension
print ('List comperhension:'.upper())
	# List comperhension origin
mylist = []
for letter in lista[0]:
  mylist.append(letter)
print (f'- List comperhension origin: {mylist}')
	# Simple list comperhension
simlistac = [letter for letter in lista[0]]
print (f'- Simple list comperhension: {simlistac}')
	# List comperhension with statements
slc = list(num**2 for num in range(0,11) if num%2==0)
print (f'- List comperhension with statements: {slc}')
# Nested Statement in List comperhension
nslc = [num if num%2==0 else 'ODD' for num in range(0,11)]
print (f'- Nested Statement in List comperhension: {nslc}')
# Nested Loop in List comperhension
nlc = [x*y for x in [2,4,6] for y in [1,10,100]]
print (f'- Nested Loop in List comperhension: {nlc}')