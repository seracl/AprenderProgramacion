### Python Touples
'''
A tuple is an ordered inmutable sequence of objects, similar to the list, but enclosed within parentheses instead. 
A tuple consists of a number of any data type and separated by commas. 
Touples cannot be updated, can be thought of as read-only lists.
'''
touple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytouple = (123, 'john')

print('Touples:')
print (touple)              # Prints complete touple
print (touple[0])           # Prints first element of the touple
print (touple[1:3])         # Prints elements starting from 2nd till 3rd 
print (touple[2:])          # Prints elements starting from 3rd element
print (tinytouple * 2)      # Prints touple two times
print (touple + tinytouple) # Prints concatenated touples

'''Touples vs lists: This would work with lists but not with inmutable touples'''
touple[2] = 1000
print(touple)               # Invalid syntax with tuple
print('\n') 