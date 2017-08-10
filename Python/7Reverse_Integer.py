"""
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
"""
# python3中用operator代替python2的cmp
import operator

class Solution(object):

    def cmp(self, a, b):
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = self.cmp(x, 0)
        # repr:一个对象转成字符串显示
        r = int(repr(s * x)[::-1])
        return s*r*(r < 2**31)
"""
    python2:
    def reverse(self, x):
        s = cmp(x, 0)
        r = int(`s*x`[::-1])
        return s*r * (r < 2**31)
"""