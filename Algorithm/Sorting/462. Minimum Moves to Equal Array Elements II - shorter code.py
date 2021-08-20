# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# Source: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/94923/2-lines-Python-2-ways

class Solution:
    def minMoves2(self, nums):
        median = sorted(nums)[len(nums) // 2]
        return sum(abs(num - median) for num in nums)