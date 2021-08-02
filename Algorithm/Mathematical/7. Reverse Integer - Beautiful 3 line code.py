#https://leetcode.com/problems/reverse-integer/
# credit: https://leetcode.com/problems/reverse-integer/discuss/132861/3-lines-Python-Solution
# https://stackoverflow.com/questions/55917667/please-explain-1-1x-0

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = [1,-1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31)-1 < rst < 2**31 else 0