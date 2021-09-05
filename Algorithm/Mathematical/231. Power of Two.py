#https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        if n==1:
            return True
        return True if n & n-1 ==0 else False