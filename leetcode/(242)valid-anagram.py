class Solution(object):
	def isAnagram(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		anagram is a word formed by rearranging the letters of a different word or phrase
		"""
		h = {}
		for ch in s:
			if ch not in h:
				h[ch] = 0
			h[ch] += 1

		# so the characters in each string balance each other out
		for ch in t:
			if ch not in h:
				h[ch] = 0
			h[ch] -= 1

		for key in h.keys():
			if h[key] != 0:
				return False

		return True

