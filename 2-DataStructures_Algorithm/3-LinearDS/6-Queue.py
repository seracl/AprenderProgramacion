# QUEQUE
"""
Basic operations:
	- Insert enqueue()
	- Delete dequeue()
	- peek()
FIFO structure: first in, first out
Can be implemented both ith dynamic arrays or linkedlists

Applications:
	- Important when implementing the Brathfurt Searcg graph algorithm
	- When a resoiurce is shared between consumers (threads) they're stored in a queue
	- CPU scheduling
	- Asynchronously transfer data (data isn't recived at the same rate as sent) between processes
	- IO buffers
	- Operational research applications or stochastic models relies on queues

"""




class Queue:

	def __init__(self):
		self.queue = []
		
	def isEmpty(self):
		return self.queue == []
		
	def enqueue(self, data):
		self.queue.append(data)
		
	def dequeue(self):
		data = self.queue[0]
		del self.queue[0]
		return data
		
	def peek(self):
		return self.queue[0]
		
	def sizeQueue(self):
		return len(self.queue)
	
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.sizeQueue())
print("Dequeue: ", queue.dequeue())
print("Dequeue: ", queue.dequeue())
print(queue.sizeQueue())