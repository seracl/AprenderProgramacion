# Python Dictionary
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

print('Dictionaries:'.upper())
print ("- Prints value for 'one' key:   {}".format(dicta['one'])) 
print ("- Prints value for 2 key:       {}".format(dicta[2])) 
print ("- Prints dicta:                 {}".format(dicta))
print ("- Prints complete dictionary:   {}".format(tinydict)) 
print ("- Prints all the keys:          {}".format(tinydict.keys())) 
print ("- Prints all the values:        {}".format(tinydict.values())) 

## Iterate through dictionary
print('Iterate through dictionary:'.upper())
print('General info om dict:')
atm = dir({})
print(f'- Length: {len(atm)}')
print(f'- Attributes list: {atm[:30]}')
print(f'- Methods list: {atm[:-12:-1]}')
print('- MA: ', list(tinydict.__iter__()))

### Iterating Through Keys Directly
print('Iterating Through Keys Directly:')
for key in tinydict:
    print ('- Key:', key)

### Iterating Through .items()
print('Iterating Through .items():')
print('  Accessing items as tuples.')
for item in tinydict.items():
    print ('- Item:', item)
print('  Tuple unpacking in dict.')
for key, value in tinydict.items():
    print (f'- Item: {key} --> {value}')

### Iterating Through .keys()
print('Iterating Through .keys():')
print('  Accessing the keys.')
for key in tinydict.keys():
    print ('- Item:', key)
print('  Accessing values through keys in dict.')
for key in tinydict.keys():
    print (f'- Item: {key} --> {tinydict[key]}')

### Iterating Through .values()
print('Iterating Through .values():')
print('  Accessing the values.')
for value in tinydict.values():
    print ('- Item:', value)
print(f'  Accessing a specific value: {"sales" in tinydict.values()}.')

## Built-in List Functions & Methods
'''
https://www.tutorialspoint.com/python/python_dictionary.htm
Functions:
- cmp(dict1, dict2) | Compares elements of both dict.
- len(dict)         | Gives the total length of the dictionary. This would be equal to the number of items in the dictionary.
- str(dict)         | Produces a printable string representation of a dictionary
- type(variable)    | Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.

Methods
- dict.clear()                       | Removes all elements of dictionary dict
- dict.copy()                        | Returns a shallow copy of dictionary dict
- dict.fromkeys()                    | Create a new dictionary with keys from seq and values set to value.
- dict.get(key, default=None)        | For key key, returns value or default if key not in dictionary
- dict.has_key(key)                  | Returns true if key in dictionary dict, false otherwise
- dict.items()                       | Returns a list of dict's (key, value) tuple pairs
- dict.keys()                        | Returns list of dictionary dict's keys
- dict.setdefault(key, default=None) | Similar to get(), but will set dict[key]=default if key is not already in dict
- dict.update(dict2)                 | Adds dictionary dict2's key-values pairs to dict
- dict.values()                      | Returns list of dictionary dict's values
'''