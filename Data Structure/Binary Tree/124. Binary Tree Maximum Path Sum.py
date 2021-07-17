# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    maxValue = -sys.maxsize -1
    def maxPathDown(self,node):
        if node == None: return 0;
        left = max(0, self.maxPathDown(node.left));
        right = max(0, self.maxPathDown(node.right));
        """The second maxValue contains the bigger between the left sub-tree and right sub-tree.
         if (left + right + node.val < maxValue ) then the result will not include the     parent node which means the maximum path is in the left branch or right branch. """
        self.maxValue = max(self.maxValue, left + right + node.val);
        return max(left, right) + node.val;
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxPathDown(root);
        return self.maxValue;