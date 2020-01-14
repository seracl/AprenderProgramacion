# Touples
"""
Sequences of immutable Python objects
Difference from list:
	- Uses  parentheses insetad square brackets 
	- Touples cannot be changed (inmutable)
"""

## Defining a touple
print('Defining a touple:'.upper())

tup_emp = ()
print (f"	- Empty touple: {tup_emp}")
tup_enval = (50,)
print (f"	- Single val touple: {tup_enval}")

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
print (f"	- Tup 1: {tup1}")
print (f"	- Tup 2: {tup2}")
print (f"	- Tup 3: {tup3}")

## Accessing Values
print('Accessing Values:'.upper())
print (f"	- tup1[0]: {tup1[0]}")
print (f"	- tup2[1:5]: {tup2[1:5]}")

## Updating Tuples
print ('Updating Tuples:'.upper())
tup3 = tup2 + tup1
print (f"	- tup3: {tup3}")

## Delete Tuple Elements
print ('Delete Tuple Elements:'.upper())
print (f"	- Original touple: {tup3}")
#del tup3
#print(f"	- Updated touple: {tup3}")

## Basic Touple Operations
print ('Basic Touple Operations:'.upper())
print (f"	- Length:         {len(tup1)}")
print (f"	- Concatenation:  {tup1 + tup2}")
print (f"	- Repetition:     {('Hi!') * 4}")
print (f"	- Membership:     {3 in tup2}")
print (f"	- Iteration:      {'for x in (1, 2, 3): print x'}")