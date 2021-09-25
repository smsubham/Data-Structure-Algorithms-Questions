#https://leetcode.com/problems/first-bad-version/
#TLE

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n):
            if isBadVersion(i):
                return i
        return n