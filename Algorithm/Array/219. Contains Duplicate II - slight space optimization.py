# https://leetcode.com/problems/contains-duplicate-ii/
# Space optimisation using a fixed-size Set with a least-recently seen Eviction Policy,
# Source: https://leetcode.com/problems/contains-duplicate-ii/discuss/61375/Python-concise-solution-with-dictionary.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i,num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False