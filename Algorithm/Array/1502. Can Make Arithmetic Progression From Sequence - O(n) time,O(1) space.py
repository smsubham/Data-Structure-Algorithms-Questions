# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
# Source: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/discuss/720200/Clean-Python-3-O(N)

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        m = min(arr)
        gap = (max(arr) - m) / (len(arr) - 1)
        if gap == 0: return True
        i = 0
        while i < len(arr):
            #if its following AP just go to next element.
            if arr[i] == m + i * gap:
                i += 1
            # else check if its valid.
            else:
                dis = arr[i] - m
                if dis % gap != 0: return False
                #Find actual position
                pos = int(dis / gap)
                #if that position element is same as current no AP possible.
                if arr[pos] == arr[i]: return False
                # Put the element in correct position
                arr[pos], arr[i] = arr[i], arr[pos]
        return True