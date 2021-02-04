class Solution(object):
	def trailingZeroes(self, n):
		"""
		:type n: int
		:rtype: int
		time: O(log n)
		trick:
			5*4*3*2*1
			in order to get 0 you always need 2 and 5
			factorial -> has a lot of 2; even numbers
			how many 5s are in your input?
			10*9*8*7*6*5*4*3*2*1
			10 = 5*2, 5   so there are two 5s
			so there are 2 trailing zeroes
		"""
		res = 0
		while n != 0:
			n = n // 5  # floor division
			res += n
		return res

