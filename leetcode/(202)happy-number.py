class Solution(object):
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""

		# determine square sum
		def sqsum(num):
			result = 0
			while num > 0:
				r = num % 10
				result = result + r * r
				num = num // 10
			return result

		seen = set()
		# to avoid going in an infinite loop (if there's a cycle)
		while sqsum(n) not in seen:
			sum1 = sqsum(n)
			# if result is 1 then we found our happy number
			if sum1 == 1:
				return True
			# if result isn't 1 keep doing sqsum of digits
			else:
				seen.add(sum1)
				n = sum1
		return False


"""
19 -> 1 9 -> 1^2 + 9^2 = 82 
      8 2 -> 8^2 + 2^2 = 68
      6 8 -> 6^2 + 8^2 = 100
      1 0 0 -> 1^2 + 0^2 + 0^2 = 1 
      happy!

splitting 19 into 1 and 9 
19 % 10 = 9 
19 // 10 = 1 

19 > 0:
    r = 19 % 10 = 9
    result = 0 + 9 * 9 = 81
    num = 19 // 10 = 1 
1 > 9:
    r = 1 % 10 = 0
    result = 81 + 1 * 1 = 82 
    num = 1 // 10 = 0 

"""
