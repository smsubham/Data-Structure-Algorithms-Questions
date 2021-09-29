#https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
class Solution:
    def guessNumber(self, n: int) -> int:
        i,j=1,n
        while i<=j:
            mid = i+(j-i)//2
            pick = guess(mid) 
            if pick == 0:
                return mid
            elif pick<0:
                j = mid -1
            else:
                i = mid+1
        return -1
