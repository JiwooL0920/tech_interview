# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
	def isSubtree(self, s, t):
		"""
		:type s: TreeNode
		:type t: TreeNode
		:rtype: bool
		time and space: O(n)      if they're skewed
		"""

		def isSame(s, t):
			# Base cases
			if s == None and t == None:
				return True
			if s == None or t == None:
				return False
			if s.val != t.val:
				return False
			# Recurse
			return isSame(s.left, t.left) and isSame(s.right, t.right)

		def traverse(s, t):
			# we didn't find any node same as the root
			if s == None:
				return False
			# we find all value is same????
			if t == None:
				return True
			return isSame(s, t) or traverse(s.left, t) or traverse(s.right, t)

		return traverse(s, t)