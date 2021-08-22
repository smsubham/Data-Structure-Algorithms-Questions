# https://leetcode.com/problems/missing-number/
# https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        #if all number from 0-n were their then this should have been the sum
        requiredSum = n*(n+1)/2
        #this is actual sum
        actualSum = sum(nums)
        return int(requiredSum - actualSum)