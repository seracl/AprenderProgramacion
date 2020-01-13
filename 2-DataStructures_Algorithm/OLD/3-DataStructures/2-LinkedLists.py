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
			- Removing first item is very fast because search is not needed, just update the reference at O(1) time complexity
  		- Removing item at given point not fast, item need be searched (by traversing the list) and reference updated at O(N) time complexity
	- Display: Displays the complete list.
	- Search: Searches an element using the given key.
	- Delete: Deletes an element using the given key.

Pros and cons
	- References wastes memory as updating references and reaching nodes (nodes are reached/searched in order) takes constant time O(1)
	- They do not allow random access, so indexing cannot be used get_item(idex)
	- Insert/removing at the beggining of the array is relativelly easy, just update the reference in O(1)[constant] complexity
	- Inserting/removing at the end is not so simple cause the whole list have to be transversed and all references have to be updated at O(N)[linear]  complexity O(1) + O(N) = O(N)
	- Removing takes O(N)/2 which results in O(N) complexity
  - Linked lists are dynamic data structures
  - Very efficient way to manipulate the first element
  - Easy implementation
  - Easy to grow organically
  - Difficult to trtansverse cause node pointer has to be changed. That can be solved with double linked lists
  - Double LL wastes even more space with back node referencing
"""

# Double linked list
"""
Doubly Linked List is a variation of Linked list in which navigation is possible in both ways.
Important terms to understand the concept of doubly linked list:
	- Link: Each link can store a data called an element.
	- Next: Each link contains a link to the next link called Next.
	- Prev: Each link contains a link to the previous link called Prev.
	- LinkedList: A Linked List contains the connection link to the first link called First and to the last link called Last.

Basic Operations
	- Insertion: Adds an element at the beginning of the list.
	- Deletion: Deletes an element at the beginning of the list.
	- Insert Last: Adds an element at the end of the list.
	- Delete Last: Deletes an element from the end of the list.
	- Insert After: Adds an element after an item of the list.
	- Delete: Deletes an element from the list using the key.
	- Display forward: Displays the complete list in a forward manner.
	- Display backward: Displays the complete list in a backward manner.
"""
# Array vs Linked List
"""
Searching
	- Searching yields the same result for both, but array is faster than l-list
	- Array allows random access getItem(index) which has O(1) complexity in comparison 
	- L-list have O(N) complexity cause of the references
	- Array is better than LL for search because it has indexing but also cause LL have to traverse all items for search
Deletion
	- Removing the first element with linked lists takes O(1) and O(N) for the last.
	- Removing the first element with array takes O(N) cause the array has to be reconstructed; removing the last takes O(1)
	- Linked lists are better for deletion, because pointers makes deletion easier
Memory management
	- Arrays do not need extra memory
	- Linked lists need extra memory because of reference/pointers
	- Arrays are more memory friendly

									| Linked Lists | Arrays |
	-----------------------------------------
	Search          |     O(N)     |  O(1)  |
	Insert at start |     O(1)     |  O(N)  |
	Insert at end   |     O(N)     |  O(1)  |
	Waste space     |     O(N)     |   0    |
"""

class Node(object):
	
	def __init__(self, data):
		"""
		Node constructor
		Contains the data and a reference to the next node
		The node reference is empty by default
		"""
		self.data = data
		self.nextNode = None

class LinkedList(object):

	def __init__(self):
		"""
		Linked List Constructor
		Store the head/first node of the linked list
		"""
		self.head = None
		self.size = 0
	
	def insertStart(self, data):
		"""
		Inserting items at the beggining of the list at O(1)
		"""
		self.size += 1
		newNode = Node(data)

		if not self.head:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			self.head = newNode
	
	def remove(self, data):
	
		if self.head is None:
			return
			
		self.size = self.size - 1
		
		currentNode = self.head
		previousNode = None
		
		while currentNode.data != data:
			previousNode = currentNode
			currentNode = currentNode.nextNode
			
		if previousNode is None:
			self.head = currentNode.nextNode
		else:
			previousNode.nextNode = currentNode.nextNode
	
	def size1(self):
		return self.size
	
	def size2(self):
		actualNode = self.head
		size = 0

		while actualNode is not None:
			size += 1
			actualNode = actualNode.nextNode
		
		return size
	
	# O(N)
	def insertEnd(self, data):
	
		self.size = self.size + 1
		newNode = Node(data)
		actualNode = self.head
		
		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode
			
		actualNode.nextNode = newNode
		
	def traverseList(self):
	
		actualNode = self.head
		
		while actualNode is not None:
			print("%d " % actualNode.data)
			actualNode = actualNode.nextNode


			
linkedlist = LinkedList()

linkedlist.insertStart(12)
linkedlist.insertStart(122)
linkedlist.insertStart(3)
linkedlist.insertEnd(31)

linkedlist.traverseList()

# linkedlist.remove(3)
# linkedlist.remove(12)
# linkedlist.remove(122)
# linkedlist.remove(31)

print(linkedlist.size1())
