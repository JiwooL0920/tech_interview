# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
	def invertTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""

		def dfs(node):
			# base case
			if not node:
				return
			# recursive call dfs on left and right
			# pre order traversal
			dfs(node.left)
			dfs(node.right)
			node.left, node.right = node.right, node.left

		dfs(root)
		return root
