#https://leetcode.com/problems/unique-binary-search-trees/
#https://leetcode.com/problems/unique-binary-search-trees/discuss/703049/Python-Math-oneliner-O(n)-using-Catalan-number-explained

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return factorial(2*n)//factorial(n)//factorial(n)//(n+1)