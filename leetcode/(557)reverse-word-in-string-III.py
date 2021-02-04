class Solution(object):
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		words = s.split()
		result = []
		for w in words:
			# start from the end towards the first taking each element. so reverse a
			result.append(w[::-1])
		return " ".join(result)

# list comprehension
# return " ".join([i[::-1] for i in s.split()])


