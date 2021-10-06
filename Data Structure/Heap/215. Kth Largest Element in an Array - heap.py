#https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/257587/Python-Priority-Queue-and-Quick-Select
#https://leetcode.com/problems/kth-largest-element-in-an-array/


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = nums[:k]
        heapq.heapify(pq)
        for x in nums[k:]:
            heapq.heappush(pq, x)
            heapq.heappop(pq)
        return pq[0]