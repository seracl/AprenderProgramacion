# *args and **kwargs
print ('*args and **kwargs:'.upper())
def myfunc (a,b, c=0, d=0, e=0):
  ''' When we wanna work with multiple positional args, they must be passed as tuples. '''
  # Returns 5% of the sum of a and b
  return sum ((a,b, c,d,e)) * 0.05 # Args passed as tuples
print('myfunc: ', myfunc(40,60))

print ('Args')
	# Allow to take an arbitrary number of arguments
def myfun(*args):
  '''
  Now we can pass as many arguments as we want.
  Python will enclose them inside a tuple before passing them
  The word args can be substituted by any word, the asterix is what defines it  
  '''
  print('Args: ', args)
  return sum (args) * 0.05
print('myfunc: ', myfun(40,60, 100, 1, 34))

print ('KWARGS:')
	# Allow to take an arbitrary number of arguments
def mykwf(** kwargs):
	'''
  Now we can pass as many arguments as we want.
  Python will enclose them inside a dictionary before passing them
  The word args can be substituted by any word, the double asterix is what defines it
  '''
	print('Kwargs: ', kwargs)

	if 'fruit' in kwargs:
		print ("My fruit is {}".format(kwargs['fruit']))
	else:
		print ('I did not find any fruit here.')

mykwf (fruit='apple', veggie='lettuce')