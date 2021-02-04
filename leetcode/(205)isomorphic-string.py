class Solution(object):
	def isIsomorphic(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		# length are not same -> not isomorphic
		if len(s) != len(t):
			return False
		s_map = {}
		t_map = {}
		for i in range(0, len(s)):
			s_ch, t_ch = s[i], t[i]
			# add new character mapping
			if s_ch not in s_map:
				s_map[s_ch] = t_ch
			if t_ch not in t_map:
				t_map[t_ch] = s_ch
			# if character in map, check if it equals to that mapping
			if t_map[t_ch] != s_ch or s_map[s_ch] != t_ch:
				return False
		return True

