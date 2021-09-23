#https://leetcode.com/problems/number-of-good-pairs/
# O(n^2) time and O(1) space.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count