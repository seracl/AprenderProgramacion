# Dictionaries
"""
Dictionaries are kind of hash table type.
Consist of key-value pairs, separated by (:) and enclosed by curly braces ({}).
The keys (strings enclosed by double quotation marks) are unique within a dictionary while values may not be.
Dictionaries have no concept of order among elements.
More than one entry per key not allowed.
Keys must be immutable.
"""
## Defining a dictionary
print('Defining a dictionary:'.upper())
dict_empty = {}
print (f"	- Empty dictionary: {dict_empty}")
dict_filled = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(f"	- Filled dictionary: {dict_filled}")
print(f"	- Dictionary keys: {dict_filled.keys()}")
print(f"	- Dictionary values: {dict_filled.values()}")

## Accessing Elements
print('Accessing Elements:'.upper())
print(f"	- dict_filled['Name']: {dict_filled['Name']}")
print(f"	- dict_filled['Age'] : {dict_filled['Age']}")

## Updating Elements
print('Updating Elements:'.upper())
dict_filled['Name'] = 'Fernando'
dict_filled['New'] = 'Manolo'
print(f"	- Dictionary name from Zara to: {dict_filled['Name']}")
print(f"	- Updated dictionary          : {dict_filled}")

## Delete Elements
print('Delete Elements:'.upper())
del dict_filled['New']
print(f"	- Updated dictionary          : {dict_filled}")

