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

print('Lists:')
print (lista)            # Prints complete list
print (lista[0])         # Prints first element of the list
print (lista[1:3])       # Prints elements starting from 2nd till 3rd 
print (lista[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (lista + tinylist) # Prints concatenated lists
print('\n') 