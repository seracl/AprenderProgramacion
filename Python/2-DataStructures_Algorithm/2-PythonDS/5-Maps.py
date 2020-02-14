# Maps
"""
Data structure to manage multiple dictionaries together as one unit.
The combined dictionary contains key and value pairs in a specific sequence eliminating any duplicate keys.
The best use of Python Maps is to search through multiple dictionaries at a time and get the proper key-value pair mapping.
Python Maps also behave as stack data structure.
"""
import collections

## Defining a map
print('Defining a map'.upper())
dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}
res = collections.ChainMap(dict1, dict2)

print (' Creating a single dictionary:')
print (f' Map = {res.maps}')
print (f' Keys = {list(res.keys())}')
print (f' Values = {list(res.values())}')
print ()

print('Print all the elements from the result:')
for key, val in res.items():
    print(f'{key} = {val}')
print()

print('Find a specific value in the result:')
print(f'day3 in res: {"day3" in res}')
print(f'day4 in res: {"day4" in res}')

## Map Reordering
print('Map Reordering'.upper())
res2 = collections.ChainMap(dict2, dict1)
print(f" res2: {list(res2)}")
print(f" res2: {res2.maps}")

## Updating Map
print('Updating Map'.upper())
dict2['day4'] = 'Fri'
print(f" res2: {res2.maps}")