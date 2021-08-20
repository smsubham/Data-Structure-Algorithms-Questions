# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
# Source: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/discuss/720200/Clean-Python-3-O(N)

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        k = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            if arr[i+1] - arr[i] != k:
                return False
        return True