# Matrix
"""
Matrix is a special case of two dimensional array where each data element is of strictly same size.
Every matrix is a two dimensional array but not vice versa.
Matrices are very important data structures for many mathematical and scientific calculations.
"""
from numpy import *


## Defining a matrix
print('Defining a matrix:'.upper())
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   		 ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   		 ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   		 ['Sun',13,15,19,16]])
    
m = reshape(a,(7,5))
print(m)

## Accessing Elements
print('Accessing Elements:'.upper())
print(f'Print data for Wednesday:\n {m[2]}')
print(f'Print data for friday evening:\n {m[4][3]}')

## Adding Elements
print('Adding Elements:'.upper())
m_r = append(m,[['Avg',12,15,13,11]],0)
print(f'	Adding a row:\n {m_r}')
m_c = insert(m,[5],[[1],[2],[3],[4],[5],[6],[7]],1)
print(f'	Adding a column:\n {m_c}')

## Deleting Elements
print('Deleting Elements:'.upper())
m = delete(m,[2],0)
print(f'	Deleting a row:\n {m}')
m = delete(m,s_[2],1)
print(f'	Deleting a column:\n {m}')

## Updating Elements
print('Updating Elements:'.upper())
m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   		 ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   		 ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   		 ['Sun',13,15,19,16]])
m[3] = ['Thu',0,0,0,0]
print(f'	Updating a row:\n {m}')
