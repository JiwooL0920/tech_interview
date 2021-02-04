# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        orig_num, new_num = x, 0
        while x:
            new_num, x = new_num*10 + x%10, x//10
        return orig_num == new_num
