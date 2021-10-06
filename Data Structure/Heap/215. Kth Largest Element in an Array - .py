#https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/1019513/Python-QuickSelect-average-O(n)-explained
#https://leetcode.com/problems/kth-largest-element-in-an-array/


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        L, M = len(left), len(mid)
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]