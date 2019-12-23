# Data types

## Integers       |  int  |: Whole numbers                          | n = 300
### int  (10)      : signed integers
### long (519...L) : long integers that can also be represented in octal and hexadecimal

## Floating Point | float |: Numbers with decimal point             | 2.3; 4.6
### float   (0.0)  : floating point real values
### complex (3.14j): complex numbers

## Strings        |  str  |: Ordered sequence of characters         | "Hello", "Sammy"

## Lists          |  list |: Ordered sequence of objects            | [10, "Hello", "20"] 
list1 = ['physics', 'chemistry', 1997, 2000];
print list1
del list1[2];
print "After deleting value at index 2 : "
print list1

## Dictionaries   |  dict |: Unordered Key:Value pairs              | {"mykey":"value","name":"Frankie"}
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']

## Touples        |  tup  |: Ordered inmutable sequence of objects  | (10,"hello")
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print tup3;

## Sets           |  set  |: Unordered collection of unique objects | {"a","b"} 

## Booleans       |  bool |: Logical TRUE or FALSE