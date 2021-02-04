class Solution(object):
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		dict = {}
		for n in nums:
			if n not in dict:
				dict[n] = 1
			# if majority element
			if dict[n] > len(nums) // 2:
				return n
			# else if n exists in dict
			dict[n] += 1
