# General Data Structures
"""
Data Structures: Programmatic way of storing data so that data can be used efficiently.

Data structures foundation terms:
	- Interface: Each data structure has an interface, or set of operations, accepted parameters and return types that a data structure supports. 
	- Implementation: Implementation provides the internal representation and the definition of the algorithms used in the operations of the data structure. 

Characteristics of a Data Structure
	- Correctness: Data structure implementation should implement its interface correctly.
	- Time Complexity: Running time or the execution time of operations of data structure must be as small as possible.
	- Space Complexity: Memory usage of a data structure operation should be as little as possible.

Execution Time Cases: Used to compare data structure's relative execution time (f(n) execution time in function of the f(data) ).
	- Worst Case: Maximum amount of time a data structure operation time can take. 
		In worst case, operations won't take more than ƒ(n) time where ƒ(n) represents function of n.
	- Average Case: Average execution time of an operation of a data structure. 
		If an operation takes ƒ(n) time in execution, then m operations will take m*ƒ(n) time.
	- Best Case: An operation's least possible execution time.
		If execution takes ƒ(n) time, then the actual operation may take time as the random number with ƒ(n) maximum time.

Data definition and data object
	Data Definition defines a particular data with the following characteristics.
		- Atomic: Definition should define a single concept.
		- Traceable: Definition should be able to be mapped to some data element.
		- Accurate: Definition should be unambiguous.
		- Clear and Concise: Definition should be understandable.
	Data Object represents an object having a data.

General Data Structures
	Liner Data Structures
		These data structures store the data elements in a sequential manner.
			- Array: Sequential arrangement of elements paired with the index of the data element.
			- Linked List: Each element contains a link to another element along with the data present in it.
			- Stack: DS which follows only to specific order of operation. LIFO(last in First Out) or FILO(First in Last Out).
			- Queue: Similar to Stack but the order of operation is only FIFO(First In First Out).
			- Matrix: Multi-dimensional data structure in which elements are referred by a pair of indices.
	Non-Liner Data Structures
		DS in which there is no sequential linking of data elements. 
		Any pair or group of data elements can be linked to each other and can be accessed without a strict sequence.
			- Binary Tree: Each element can be connected to maximum two other elements and it starts with a root node.
			- Heap: It is a special case of Tree DS where the data in the parent node is either strictly greater than/ equal to the child nodes or strictly less than it’s child nodes.
			- Hash Table: DS which is made of arrays associated with each other using a hash function. It retrieves values using keys rather than index from a data element.
			- Graph: It is an arrangement of vertices and nodes where some of the nodes are connected to each other through links.
	Python Specific Data Structures
		- List: Similar to array but the data elements can be of different data types.
		- Tuple: Similar to lists but they are immutable which means the values cannot be modified they can only be read.
		- Dictionary: The dictionary contains Key-value pairs as its data elements.

Basic Operations 
	The data structure chosen depends on the frequency of the operation to be performed on it.
		- Traversing
		- Searching
		- Insertion
		- Deletion
		- Sorting
		- Merging
"""