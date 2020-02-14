# Sets
"""
A set is a collection of items not in any particular order.
	- The elements in the set cannot be duplicates.
	- The elements in the set are immutable(cannot be modified) but the set as a whole is mutable.
	- There is no index attached to any element in a python set. So they do not support any indexing or slicing operation.

Sets in python are typically used for mathematical operations:
	- Union
	- Intersection
	- Difference
	- Complement
"""
## Defining a set
print('Defining a set:'.upper())
empty_set = set()
print(f"	- Empty dictionary: {empty_set}")
Days = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months = {"Jan","Feb","Mar"}
Dates = {21,22,17}
print(Days)
print(Months)
print(Dates)

## Accessing Elements
print('Accessing Elements:'.upper())
'''Individual values cannot access. One can only access all the elements together'''
for d in Days:
	print(d)

## Adding Items to a Set
print('Adding Items to a Set:'.upper())
'''Using add() method, there is no specific index attached to the newly added element'''
Days.add("Sun")
print(Days)

## Removing Item from a Set
print('Removing Item from a Set:'.upper())
'''Using discard() method, there is no specific index attached to the newly added element'''
Days.discard("Sun")
print(Days)

## Union of Sets
print('Union of Sets:'.upper())
set_union = Months|Dates
print(set_union)

## Intersection of Sets
print('Intersection of Sets:'.upper())
set_intersect = set_union & Dates
print(set_intersect)

## Difference of Sets
print('Difference of Sets:'.upper())
set_diff = set_union - Dates
print(set_diff)

## Compare of Sets
print('Compare of Sets:'.upper())
set_supercomp = set_union <= Dates
set_undercomp = set_union >= Dates
print(set_supercomp)
print(set_undercomp)