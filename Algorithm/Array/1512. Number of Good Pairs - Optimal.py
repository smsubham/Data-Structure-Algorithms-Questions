#https://leetcode.com/problems/number-of-good-pairs/
#https://leetcode.com/problems/number-of-good-pairs/discuss/731561/JavaC%2B%2BPython-Count
"""
Complexity
Time O(N)
Space O(N)
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return int(sum(k * (k - 1) / 2 for k in collections.Counter(nums).values()))