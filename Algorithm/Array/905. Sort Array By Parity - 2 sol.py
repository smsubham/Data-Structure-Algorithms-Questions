#https://leetcode.com/problems/sort-array-by-parity/


#Approach 1: Sort

class Solution(object):
    def sortArrayByParity(self, A):
        A.sort(key = lambda x: x % 2)
        return A

"""
Approach 2: Two Pass
Intuition and Algorithm
Write all the even elements first, then write all the odd elements.
"""

class Solution(object):
    def sortArrayByParity(self, A):
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])

