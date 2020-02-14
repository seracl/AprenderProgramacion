# Map Function

my_nums = [1,2,3,4,5,6]
names = ['Andy', 'Eve', 'Sally']

def square(num):
  return num**2

def splicer (mystring):
  if len(mystring)%2 == 0:
    return 'EVEN'
  else:
    return mystring[0]

print ('The map function'.upper())
'''
Used to itera through the elements of a given data type
The function is passed as argument but not initialized cause the map function will do that at given time 
'''

print (f'Memory location of the map() function: {map(square, my_nums)}')
 # In order to acces the values one has to iterate or cast the function

print ('Iterating through items.')
for item in map(square, my_nums):
  print ('- Item: ', item)
  
print ('Casting the function')
print (f'- Casting the map() function into a list: {list(map(square, my_nums))}')
print (f'- Casting the map() function into a list: {list(map(splicer, names))}')

# The filter function
print ('The filter function'.upper())
'''
Used to iterate through a given iterable and yield those elements that follow a certain condition.
The function is passed as argument but not initialized as with the amp function 
'''

def check_even (num):
  return num%2 == 0
print (f'- Casting the filter() function into a list: {list(filter(check_even, my_nums))}')

# The lambda expression
'''
Also know as anonymous function
Is intended to be only used one time
Doesnt have a name nor use the def keyword
'''
print ('The lambda expression'.upper())
print ('The original lambda expression:')

def square (num):
  result = num ** 2
  return result
print (f'- Function from which lambda implementation will be explained: {square(3)}')

def square1l (num): return num ** 2
print (f'- One line implementation: {square1l(3)}')

squack = lambda num: num ** 2
print (f'- Lambda expression implementation: {squack(3)}')

print ('Lambda expression with map() and filter()')
print (f'- Lambda expression with map() implementation: {list(map(lambda num: num ** 2, my_nums))}')
print (f'- Lambda expression with filter() implementation: {list(filter(lambda num: num%2 == 0, my_nums))}')