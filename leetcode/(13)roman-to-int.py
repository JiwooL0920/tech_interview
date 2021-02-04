class Solution:
	def romanToInt(self, s):
		dic = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
		result = 0
		for i in range(len(s) - 1):
			current = dic[s[i]]
			next = dic[s[i + 1]]
			if (current >= next):
				result += current
			else:
				result -= current
		result += dic[s[len(s) - 1]]
		return result


"""
LVIII
result = 0
    current = L = 50
    next = V = 5
    current >= next
    result = 50
current = V = 5
next = I
current >= next
result = 55
    current = I
    next = I
    current >= next
    result = 56
current = I 
next = I
current >= next
result = 57

exit for loop
current = I
result = 58 

XIV = 14
current = X = 10
next = I = 1
current >= next
result = 10 
    current = I 
    next = V
    current < next
    reslt = 9
last = 5
result = 14
"""