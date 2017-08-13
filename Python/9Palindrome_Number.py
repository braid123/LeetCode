"""
Determine whether an integer is a palindrome. Do this without extra space.
判断输入数字是否是回文数
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if repr(x) == repr(x)[::-1]:
            return True
        else:
            return False