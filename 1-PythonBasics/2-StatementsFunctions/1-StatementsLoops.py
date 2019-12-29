# Control flow: 

## Statements
'''
Decision making is anticipation of conditions occurring 
	while execution of the program and specifying actions taken according to the conditions.

Python programming language provides following types of decision making statements:
- if statements        | An if statement consists of a boolean expression followed by one or more statements.
- if...else statements | An if statement can be followed by an optional else statement, which executes when the boolean expression is FALSE.
- nested if statements | You can use one if or else if statement inside another if or else if statement(s).

Statements Syntax
	if some_condition:
		# Do something
	elif some_other_condition:
			# Do something else
	else:
		# Do something different

'''

## Loops
'''
A loop statement allows us to execute a statement or group of statements multiple times.
Python provides following types of loops to handle looping requirements:
- While: Repeats a statement or group of statements while a given condition is TRUE. 
		It tests the condition before executing the loop body.
		Syntax:
		while some_boolean_condition:
			# Do something
		else:
			# Do something different
- For: Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.
- Nested: You can use one or more loop inside any another while, for or do..while loop.
'''

### Break, continue, pass
'''
These statements are used to add functionality to our loops:
- Break:    Breaks out of the current enclosing loop.
- Continue: Goes to the top of the closest enclosing loop.
- Pass:     Does nothing at all. Also used as place holder when declaring functions to be implemented on later stage.
'''

mystring = 'Sammy'

print ('Continue:'.upper())
for letter in mystring: # This is the enclosing loop
	if letter == 'a': # This one is just a statement
			continue # Go to the top of the enclosing loop
	print (letter)

print ('Break:'.upper()) 
for letter in mystring: # This is the enclosing loop
	if letter == 'a':
			break # Breaks out of the current closest enclosing loop
	print (letter)

print ('\t')
### Tuple unpacking while looping
print ('Tuple unpacking while looping:'.upper())

print ('Exempel 1:')
for item in enumerate(mystring):
  print (item)

print ('Exempel 2:')
for index,letter in enumerate(mystring):
  print (index)
  print (letter)
  
print ('\t')
### Zip function
print ('Zip function:'.upper())
mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c','d']
mylist3 = [100, 200, 300]

print ('Exempel 1:') # Memory allocation returned
print(zip(mylist1,mylist2))

print ('Exempel 2:')
for item in zip(mylist1,mylist2,mylist3):
  print (item)
print ('Exempel 3:') # Memory allocation returned
print(zip(mylist1,mylist2))

print ('\t')
### Casting
print ('Casting:'.upper())
print(list(zip(mylist1,mylist2)))

print ('\t')
### The in operator
print ('The in operator:'.upper())
print('- The x in mylist1: {}'.format('x' in mylist1))
print(f"- The x in mylist2: {'x' in mylist2}.")
d = {'mkeys':345, 'mk2':'Locura', 'mk3':300.09}
print('- The in operator in dictionaries: {}'.format('mkeys' in d))
print('- In in dictionary keys: {}'.format('mkeys' in d.keys()))

print ('\t')
### Input
results = input('What is your name?')
print(results)