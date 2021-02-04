class Solution(object):
	def canPlaceFlowers(self, a, n):
		"""
		:type flowerbed: List[int]
		:type n: int
		:rtype: bool

		You have a long flowerbed in which some of the plots are planted,
		and some are not. However, flowers cannot be planted in adjacent plots.

		Given an integer array flowerbed containing 0's and 1's, where 0
		means empty and 1 means not empty, and an integer n, return if n new
		flowers can be planted in the flowerbed without violating the no-
		adjacent-flowers rule.

		[1,0,0,0,1]
		n = 1
		we can do [1,0,1,0,1]    no consecutive 1's
		if a[i] = 0 we might be able to put a flower
		then we need to check if a[i-1] and a[i+1] are 0

		edge cases:
		i = 0, check a[i+1] is 0
		i = len-1, check a[i-1] is 0

		time: iterate array once O(n)
		space: O(1)
		"""

		count = 0
		for i in range(len(a)):
			if (a[i] == 0) and (i == 0 or a[i - 1] == 0) and (i == n - 1 or a[i + 1] == 0):
				a[i] = 1
				count += 1
		return count >= n


