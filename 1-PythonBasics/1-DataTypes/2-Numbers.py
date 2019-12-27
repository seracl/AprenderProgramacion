### Python Numbers
'''
Number objects are created when you assign a value to them.
Python supports four different numerical types:
	int (signed integers)
	long (long integers, they can also be represented in octal and hexadecimal)
	float (floating point real values)
	complex (complex numbers)
'''
var1 = 1
var2 = 10

## Number Type Conversion
'''
Python converts numbers internally, but sometimesyou need to coerce a number explicitly from one type to another.
- Type int(x) to convert x to a plain integer.
- Type long(x) to convert x to a long integer.
- Type float(x) to convert x to a floating-point number.
- Type complex(x) to convert x to a complex number with real part x and imaginary part zero.
- Type complex(x, y) to convert x and y to a complex number with real part x and imaginary part y. x and y are numeric expressions
'''
a = '1000'
b = int(a)
c = float(a)
# d = long(a) # This one seems to be discontinuated
e = complex(a)
f = complex(int(a), b)
print('Conversions:'.upper())
print(a)
print('B is equal to %i of type %s' % ( b, type(b) ))
print(f'B is as avobe, equal to {b} of type {type(b)}')
print(f'C is equal to {c} of type {type(c)}')
print(f'C is equal to {e} of type {type(e)}')
print(f'C is equal to {f} of type {type(f)}')

## Built-in functions
'''
Python includes following functions: (https://www.tutorialspoint.com/python/python_numbers.htm)
- Mathematical.
- Random Number.
- Trigonometric.
- Mathematical constants
'''