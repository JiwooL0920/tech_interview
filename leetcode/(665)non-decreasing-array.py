class Solution(object):
	def checkPossibility(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool

		Given an array nums with n integers, your task is to check
		if it could become non-decreasing by modifying at most one
		element.

		We define an array is non-decreasing if nums[i] <= nums[i + 1]
		holds for every i (0-based) such that (0 <= i <= n - 2)

		[4,2,3]
		 i
		[2,2,3]
		true

		[4,2,1]
		 i
		[2,2,1]
		   i
		2 < 1
		count = 2
		false
		"""
		count = 0
		for i in range(len(nums) - 1):
			# there is an inversion
			if nums[i] > nums[i + 1]:
				count += 1
				# if there are more than 1 inversion, return false
				if count > 1:
					return False
				if i > 0 and nums[i - 1] > nums[i + 1]:
					nums[i + 1] = nums[i]
				else:
					nums[i] = nums[i + 1]
		return True

