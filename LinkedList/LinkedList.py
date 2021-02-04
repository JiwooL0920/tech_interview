class Node:
	def __init__(self, data=None, next = None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def print(self):
		if (self.head == None):
			print("Linked list is empty")
			return
		itr = self.head
		llstr = ''
		while itr:
			llstr += str(itr.data) + " --> "
			itr = itr.next
		print(llstr)

	def insert_at_beginning(self,data):
		node = Node(data, self.head)
		self.head = node

	def insert_at_end(self,data):
		if (self.head == None):
			self.head = Node(data,None)
			return
		itr = self.head
		while itr.next: #has some value
			itr = itr.next
		itr.next = Node(data,None)

	def insert_values(self,data_list):
		self.head = None
		for data in data_list:
			self.insert_at_end(data)

	def get_length(self):
		count = 0
		itr = self.head
		while itr:
			count += 1
			itr = itr.next
		return count

	def remove_at(self, index):
		# valid index?
		if (index<0 or index>=self.get_length()):
			raise Exception("Invalid index")
		# remove head?
		if index == 0:
			self.head = self.head.next #point to next element
			return
		# otherwise
		count = 0
		itr = self.head
		while itr:
			if (count == index-1):
				itr.next = itr.next.next
				break
			itr = itr.next
			count += 1

	def insert_at(self, index, data):
		if (index<0 or index>self.get_length()):
			raise Exception("Invalid Index")
		if (index == 0):
			self.insert_at_beginning(data)
			return
		count = 0
		itr = self.head
		while (itr):
			if (count == index-1):
				node = Node(data, itr.next)
				itr.next = node
				break
			itr = itr.next
			count += 1

	def insert_after_value(self, data_after, data_to_insert):
		# search for first occurence of data_after value in linked list
		# now insert data_to_insert after data_after node
		itr = self.head
		while (itr):
			if (itr.data == data_after):
				new_data = Node(data_to_insert, itr.next)
				itr.next = new_data
				break
			itr = itr.next

	def remove_by_value(self, data):
		# remove first node that contains data
		itr = self.head
		while (itr):
			if (itr.next.data == data):
				itr.next = itr.next.next
				break
			itr = itr.next
		pass

if __name__ == '__main__':
	ll = LinkedList()
	ll.insert_at_beginning(2)
	ll.insert_at_beginning(1)
	ll.insert_at_end(3)
	ll.print()

	l2 = LinkedList()
	l2.insert_values(["hello","world","!"])
	l2.print()
	print(l2.get_length())

	ll.remove_at(2)
	ll.print()

	ll.insert_at(1,3)
	ll.print()

	ll.insert_after_value(3,5)
	ll.print()

	ll.remove_by_value(3)
	ll.print()