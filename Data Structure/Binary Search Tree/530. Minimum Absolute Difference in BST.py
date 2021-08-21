# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# Reference: https://leetcode.com/problems/minimum-absolute-difference-in-bst/discuss/99905/Two-Solutions-in-order-traversal-and-a-more-general-way-using-TreeSet
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    min_diff = sys.maxsize
    prev = None
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root == None: return self.min_diff
        self.getMinimumDifference(root.left)
        if self.prev != None:
            self.min_diff = min(self.min_diff, root.val - self.prev)
        self.prev = root.val
        self.getMinimumDifference(root.right)
        return self.min_diff