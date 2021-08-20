# https://leetcode.com/problems/contains-duplicate/

# We are forming whole set always which isn't optimal though time complexity is O(n).

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))