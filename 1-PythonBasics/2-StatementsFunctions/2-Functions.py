# Functions
'''
A block of organized and, reusable code that is used to perform a single, related action.
They provide modularity for your application and a high degree of code reusing.
Syntax:
def functionname ( parameters ):
   """
   DOCSTRING: INformation about the function
   INPUT: ...
   OUTPUT: ...
   """
   function_suite
   return [expression]
'''

# Calling a function
'''
Defining a function only gives it a name, its parameters and structures the blocks of code.
To execute it, one has to call it from a variable or another function like main() or name==main.
'''
print('Calling a function:'.upper())


def printme(st):
    "This prints a passed string into this function"
    print(st)
    return


printme("I'm first call to user defined function!")
printme("Again second call to the same function")


# Pass by reference vs value
'''
All parameters (arguments) in the Python language are passed by reference. 
It means if you change what a parameter refers to within a function.
'''
print("\t")
print('Pass by reference vs value:'.upper())


def changeme(mylist):
    '''
    All parameters (arguments) in the Python language are passed by reference. 
    It means if you change what a parameter refers to within a function, the change also reflects back in the calling function
    '''
    mylist.append([1, 2, 3, 4])
    print("Values inside the function: ", mylist)
    return


mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)

print(' Passed by value:')


def changeme(mylist):
    "This changes a passed list into this function"
    mylist = [1, 2, 3, 4]  # This would assig new reference in mylist
    print("Values inside the function: ", mylist)
    return


mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)

print(' Taping into the docstring:')
help(changeme)

# Scope
print("\t")
print('Scope'.upper())
''' 
LEGB Rule:
- Local: Names ddeclared within a function (def or lambda) and not declared global in that function (global var)
- Enclosing function locals: Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
- Global (module): Names assigned at the top-level of a module file, or declared global in a def within the file.
- Built-in (Python): Names preassigned in a built-in names module (open, range, SyntaxError)
'''
print('Local:')
print('- The first num variable is local: {}'.format('lambda num:num**2'))

print('Enclosing, Global:')
name = '- THIS IS A GLOBAL STRING'

def greet():
  # Name can also be set globally here: global name
  name = 'Enclosing'
  
  def hello():
    name = 'LOCAL'
    print (f'- This variable is {name}, to the hello function.')
  hello()
greet()

# Enclosing
print('Enclosing:')

# Global
print('Global:')

# Built-in
print('Built-in:')


def main():
    print("This is the main function")


main()


'''if __name__=='__main__':
    print("This is the main function")
    hello()'''
