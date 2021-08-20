# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
# Source: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/discuss/720200/Clean-Python-3-O(N)

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        m = min(arr)
        gap = (max(arr) - m) / (len(arr) - 1)
        if gap == 0: return True
        s = set(num - m for num in arr)
        return len(s) == len(arr) and all(diff % gap == 0 for diff in s)