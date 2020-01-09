# Linked Lists
"""
Sequence of data structures that are connected together via links (references/pointers).

Links contain items when the first node is called head and the last link points to null.
	- Link:			  Each link of a linked list can store a data called an element.
	- Next:			  Each link of a linked list contains a link to the next link called Next.
	- LinkedList: A Linked List contains the connection link to the first link called First.

Types of Linked List
	- Simple:	  Item navigation is forward only.
	- Doubly:	  Items can be navigated forward and backward.
	- Circular: Last item contains link of the first element as next and the first element has a link to the last element as previous.

Basic Operations
	- Insertion: Adds an element at the beginning of the list.
	- Deletion: Deletes an element at the beginning of the list.
	- Display: Displays the complete list.
	- Search: Searches an element using the given key.
	- Delete: Deletes an element using the given key.

Pros and cons
	- Updating references take constant time O(1)
	- Insert/removing at the beggining of the array is relativelly easy, just update the reference in O(1)[constant] complexity
	- Inserting/removing at the end is not so simple cause the whole list have to be transversed and all references have to be updated at O(N)[linear]  complexity O(1) + O(N) = O(N)
	- Removing takes O(N)/2 which results in O(N) complexity
"""

# Double linked list
"""

"""
