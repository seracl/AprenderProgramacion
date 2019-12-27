### Python Dictionary
'''
Dictionaries are kind of hash table type.
Consist of key-value pairs, and are enclosed by curly braces ({ }).
The keys are strings enclosed by double quotation marks, as the values can be of any arbitrary Python object.
Dictionaries have no concept of order among elements.
'''
dicta = {}
dicta['one'] = "This is one"
dicta[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print('Dictionaries:')
print (dicta['one'])       # Prints value for 'one' key
print (dicta[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values
print('\n') 