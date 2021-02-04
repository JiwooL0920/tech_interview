class Solution:
	def two_sum(self,nums, target):
		# return 2 indices such that they add up to specific target
		compliments = {} #hashmap
		result = []
		for index, num in enumerate(nums):
			if compliments.get(num) is None:
				compliments[target-num] = index
			else:
				result = [compliments[num], index]
		return result
