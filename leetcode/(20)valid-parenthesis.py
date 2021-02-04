class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		stack = []
		for i in range(len(s)):
			c = s[i]
			if c == '(' or c == '{' or c == '[':
				stack.append(c)
			else:
				# empty stack means there was no opening bracket before
				if len(stack) == 0:
					return False
				elif c == ')':
					if stack.pop() != '(':
						return False
				elif c == '}':
					if stack.pop() != '{':
						return False
				elif c == ']':
					if stack.pop() != "[":
						return False
		return len(stack) == 0
