# Python Strings
### https://www.tutorialspoint.com/python/python_strings.htm
'''
Strings are contiguous and ordered sequence of characters represented in the quotation marks (single or double).
	Indexing, subsetting and slicing can be performed with the operators operator ([ ] or [:] ).
    Indexing start at 0 in the beginning and -1 at the end of the string
    The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator.
'''
str = 'Hello World!!!'

print ('Strings general:'.upper())
print ('Accessing Values in Strings:')
print ("- Prints complete string:                     {}".format(str))  
print ("- Prints first character of the string:       {}".format(str[0]))  
print ("- Prints characters starting from 3rd to 5th: {}".format(str[2:5]))
print ("- Prints string starting from 3rd character:  {}".format(str[2:]))          
print ("- Prints string two times:                    {}".format(str * 2))
print ('Updating Strings:')
print ("- Prints concatenated string:                 {}".format(str + "TEST"))
print ("- Updating string:                            {}".format(str[:6] + "Python"))
print ('\n') 

## Escape Characters
'''
- \a | Bell or alert
- \b | Backspace
- \e | Escape
- \f | Formfeed
- \n | Newline
- \s | Space
- \t | Tab
- \v | Vertical tab
- \x | Character x
'''

## String Formatting Operator
'''
- %c | Character
- %s | string conversion via str() prior to formatting
- %i | signed decimal integer
- %d | signed decimal integer
- %u | unsigned decimal integer
- %o | octal integer
- %x | hexadecimal integer (lowercase letters)
- %X | hexadecimal integer (UPPERcase letters)
- %e | exponential notation (with lowercase 'e')
- %E | exponential notation (with UPPERcase 'E')
- %f | floating point real number
- %g | the shorter of %f and %e
- %G | the shorter of %f and %E
'''