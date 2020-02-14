# Hash Table
# https://www.youtube.com/watch?v=zHi5v78W1f0
# https://www.youtube.com/watch?v=MfhjkfocRR0
# https://www.youtube.com/watch?v=b4b8ktEV4Bg look

# Capacity for internal array
INITIAL_CAPACITY = 50

# Node data structure - essentially a LinkedList node
class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
	def __str__(self):
		return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next != None)
	def __repr__(self):
		return str(self)
# Hash table with separate chaining
class HashTable:
	# Initialize hash table
	def __init__(self):
		self.capacity = INITIAL_CAPACITY
		self.size = 0
		self.buckets = [None]*self.capacity
	# Generate a hash for a given key
	# Input:  key - string
	# Output: Index from 0 to self.capacity
	def hash(self, key):
		hashsum = 0
		# For each character in the key
		for idx, c in enumerate(key):
			# Add (index + length of key) ^ (current char code)
			hashsum += (idx + len(key)) ** ord(c)
			# Perform modulus to keep hashsum in range [0, self.capacity - 1]
			hashsum = hashsum % self.capacity
		return hashsum

	# Insert a key,value pair to the hashtable
	# Input:  key - string
	# 		  value - anything
	# Output: void
	def insert(self, key, value):
		# 1. Increment size
		self.size += 1
		# 2. Compute index of key
		index = self.hash(key)
		# Go to the node corresponding to the hash
		node = self.buckets[index]
		# 3. If bucket is empty:
		if node is None:
			# Create node, add it, return
			self.buckets[index] = Node(key, value)
			return
		# 4. Iterate to the end of the linked list at provided index
		prev = node
		while node is not None:
			prev = node
			node = node.next
		# Add a new node at the end of the list with provided key/value
		prev.next = Node(key, value)

	# Find a data value based on key
	# Input:  key - string
	# Output: value stored under "key" or None if not found
	def find(self, key):
		# 1. Compute hash
		index = self.hash(key)
		# 2. Go to first node in list at bucket
		node = self.buckets[index]
		# 3. Traverse the linked list at this node
		while node is not None and node.key != key:
			node = node.next
		# 4. Now, node is the requested key/value pair or None
		if node is None:
			# Not found
			return None
		else:
			# Found - return the data value
			return node.value

	# Remove node stored at key
	# Input:  key - string
	# Output: removed data value or None if not found
	def remove(self, key):
		# 1. Compute hash
		index = self.hash(key)
		node = self.buckets[index]
		prev = None
		# 2. Iterate to the requested node
		while node is not None and node.key != key:
			prev = node
			node = node.next
		# Now, node is either the requested node or none
		if node is None:
			# 3. Key not found
			return None
		else:
			# 4. The key was found.
			self.size -= 1
			result = node.value
			# Delete this element in linked list
			if prev is None:
				self.buckets[index] = node.next # May be None, or the next match
			else:
				prev.next = prev.next.next # LinkedList delete by skipping over
			# Return the deleted result 
			return result

from hashtable import HashTable
import unittest

class TestHashTable(unittest.TestCase):
	def setUp(self):
		self.ht = HashTable()
	def test_hash(self):
		self.assertEqual(self.ht.hash("hello"), self.ht.hash("hello"))
		self.assertTrue(self.ht.hash("hello") < self.ht.capacity)
	def test_insert(self):
		self.assertEqual(self.ht.size, 0)
		self.ht.insert("test_key", "test_value")
		self.assertEqual(self.ht.size, 1)
		self.assertEqual(self.ht.buckets[self.ht.hash("test_key")].value, "test_value")
	def test_find(self):
		self.assertEqual(self.ht.size, 0)
		obj = "hello"
		self.ht.insert("key1", obj)
		self.assertEqual(obj, self.ht.find("key1"))
		obj = ["this", "is", "a", "list"]
		self.ht.insert("key2", obj)
		self.assertEqual(obj, self.ht.find("key2"))
	def test_remove(self):
		self.assertEqual(self.ht.size, 0)
		obj = "test object"
		self.ht.insert("key1", obj)
		self.assertEqual(1, self.ht.size)
		self.assertEqual(obj, self.ht.remove("key1"))
		self.assertEqual(0, self.ht.size)
		self.assertEqual(None, self.ht.remove("some random key"))
	def test_capacity(self):
		# Test all public methods in one run at a large capacity
		for i in range(0,1000):
			self.assertEqual(i, self.ht.size)
			self.ht.insert("key" + str(i), "value")
		self.assertEqual(self.ht.size, 1000)
		for i in range(0,1000):
			self.assertEqual(1000-i, self.ht.size)
			self.assertEqual(self.ht.find("key" + str(i)), self.ht.remove("key" + str(i)))
	def test_issue2(self):
		self.assertEqual(self.ht.size, 0)
		self.ht.insert('A', 5)
		self.assertEqual(self.ht.size, 1)
		self.ht.insert('B', 10)
		self.assertEqual(self.ht.size, 2)
		self.ht.insert('Ball', 'hello')
		self.assertEqual(self.ht.size, 3)

		self.assertEqual(5, self.ht.remove('A'))
		self.assertEqual(self.ht.size, 2)
		self.assertEqual(None, self.ht.remove('A'))
		self.assertEqual(self.ht.size, 2)
		self.assertEqual(None, self.ht.remove('A'))
		self.assertEqual(self.ht.size, 2)