#https://leetcode.com/problems/all-possible-full-binary-trees/
#https://leetcode.com/problems/all-possible-full-binary-trees/discuss/167402/c%2B%2B-c-java-and-pything-recursive-and-iterative-solutions.-Doesn't-create-Frankenstein-trees

"""
Some good observations from above link:
Details
Similar to unique binary search trees I see a lot of peoples solutions either return a list of strange Frankenstein trees that are connected to each other and sharing branches or just straight up leak memory all over the place.

Frankenstein trees are bad because you have this weird and I dare say unexpected list of trees that are actually linked to each other. The nightmare of deleting these trees is not something I would want to deal with.

Memory leaks are also obviously a bad thing.

My solutions deal with both of these problems in different ways, so I will describe that below and instead focus on the basic idea of my solution.

For starters a full BST must have an odd number of nodes. So any even N is trivial empty return.

For the odd N solution, I felt it is easier to imagine the nodes have actual values from 1 to N. To see why, consider the list of node values [1, 2, 3, 4, 5], if we pick a root node of 3, then we can see things break down quickly. Because the left branch must be build from [1, 2] while the right must use [4, 5], but neither branch can be a full BST because there is an even number of nodes to use. If you follow this logic you can see that root node must be even, and further that each branch's root must also be even. Infact all internal nodes must be even, while all leaf nodes must be odd.

With this knowledge, we can see that all our example trees must either have 2 or 4 as the root node. Starting with 2, that makes the left branch easy as there is only the 1 node, while the right branch must use [3, 4, 5]. [3, 4, 5] is also easy since we know the 4 must be the internal, right root, node. It follows that we can solve for N if we know all the possible trees using from 1 to N - 2 nodes. Hence the answer to N can be built up by calculating the answers for all odd numbers less than N. We have something we can recurse on.

"""


#https://leetcode.com/problems/all-possible-full-binary-trees/discuss/163429/Simple-Python-recursive-solution.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        N -= 1
        if N == 0: return [TreeNode(0)]
        ret = []
        for l in range(1, min(20, N), 2):
            for left in self.allPossibleFBT(l):
                for right in self.allPossibleFBT(N - l):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ret += [root]
        return ret