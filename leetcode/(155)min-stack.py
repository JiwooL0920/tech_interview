class MinStack(object):

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.s = []  # stack
		self.minVal = float("inf")  # min value

	def push(self, x):
		"""
		:type x: int
		:rtype: None
		"""
		self.s.append(x)
		if x < self.minVal:
			self.minVal = x

	def updateMin(self):
		newMin = float("inf")
		for item in self.s:
			if item < newMin:
				newMin = item
		self.minVal = newMin

	def pop(self):
		"""
		:rtype: None, O(n)
		"""
		item = self.s.pop()
		# if the item we popped was the minimum, we need to update the min
		if item == self.minVal:
			self.updateMin()
		return item

	def top(self):
		"""
		:rtype: int,
		"""
		return self.s[-1]  # return last indexed item in the stack

	def getMin(self):
		"""
		:rtype: int,  O(1)
		"""
		return self.minVal

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()