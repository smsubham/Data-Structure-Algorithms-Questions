# https://leetcode.com/problems/contains-duplicate-ii/
# Source: https://leetcode.com/problems/contains-duplicate-ii/discuss/61375/Python-concise-solution-with-dictionary

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for i,value in enumerate(nums):
            if value in dict and i - dict[value] <=k:
                return True
            dict[value] = i
        return False