# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# Explanation: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/discuss/93817/It-is-a-math-question
# Source: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/discuss/272994/Python-Greedy-Sum-Min*Len

class Solution:
    def minMoves(self, nums: List[int]) -> int:
       	return sum(nums) - min(nums)*len(nums) 