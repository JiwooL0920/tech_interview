class Solution(object):
	def countPrimes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# time: O(n^2)
		# if n < 2:
		#     return 0
		# def isPrime(num):
		#     for i in range(2, num):
		#         if num % i == 0:
		#             return False
		#     return True
		# count = 0
		# for i in range(2,n):
		#     if isPrime(i):
		#         count += 1
		# return count

		"""
		Sieve of Eratosthenes
		n = 10 
			 0 1 2 3 4 5 6 7 8 9 10
		a = [T,T,T,T,T,T,T,T,T,T,T]
			[F,F,T,T,F,T,F,T,F,F,F]
		"""
		if n < 2:
			return 0
		a = [True] * (n + 1)  # initialize array
		a[0] = False
		a[1] = False
		count = 0
		for i in range(2, n):  # 2 * 4 = 4 * 2 j
			for j in range(i * i, n, i):
				a[j] = False
		for i in range(n):
			if a[i]:
				count += 1
		return count