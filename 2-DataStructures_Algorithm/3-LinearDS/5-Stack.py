
# Stack 
"""
Arranging objects on over another, the same way memory is allocated in this data structure.
So stack data strcuture allows operations at one end wich can be called top of the stack.
We can add elements or remove elements only form this en dof the stack.

Stacks and queues are abstract data types. The underlying data structure can be an array or a linked list

Applications:
	-> Back buttons in web browsers:
		- Terectly visited URL's are pushed onto a stack and the back button pops them
	-> Undo operations in softwares
	-> Stack memory stores local variables and function calls

"""

class Stack:
	def __init__(self):
		self.stack = []

	def isEmpty(self):
		return self.stack == []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		item = self.stack[-1]
		del self.stack[-1]
		return item

	def peek(self):
		return self.stack[len(self.stack)-1]

	def sizeStack(self):
		return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.sizeStack())
print("Popped: ", stack.pop())
print("Popped: ", stack.pop())
print(stack.sizeStack())
print("Peek:", stack.peek())
print(stack.sizeStack())