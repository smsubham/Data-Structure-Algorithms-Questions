#https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap, read chunks of array that fit into the memory, and record the intersections.

If both nums1 and nums2 are so huge that neither fit into the memory, sort them individually (external sort), then read 2 elements from each array at a time in memory, record intersections.
"""

class Solution(object):
    def intersect(self, nums1, nums2):

        counts = {}
        res = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1

        return res