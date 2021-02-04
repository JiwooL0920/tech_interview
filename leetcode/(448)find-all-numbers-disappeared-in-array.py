# from collections import Counter

class Solution(object):
	def findDisappearedNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		O(n)
		Find all the elements of [1, n] inclusive that do not appear in this array.
		input: [4,3,2,7,8,2,3,1]
		output: [5,6]
		"""
		# a container that stores elements as dictionary keys, and their
		# counts are stored as dictionary values
		# Counter({2: 2, 3: 2, 1: 1, 4: 1, 7: 1, 8: 1})
		d = collections.Counter(nums)
		# plus 1 because it includes n
		return [x for x in range(1, len(nums) + 1) if x not in d]
