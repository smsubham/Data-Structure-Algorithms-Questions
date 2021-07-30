# https://www.lintcode.com/problem/900/
# https://leetcode.com/problems/closest-binary-search-tree-value/ (premium)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import math 
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    margin = math.inf
    current = 0
    def closestValue(self, root, target):
        # write your code here
        if root == None:
            return
        
        if target == root.val:
            self.current = target
            return
        elif target > root.val:
            if abs(target -root.val)<self.margin:
                self.margin = abs(target -root.val)
                self.current = root.val
            self.closestValue(root.right,target)
        else:
            if abs(target -root.val)<self.margin:
                self.margin = abs(target -root.val)
                self.current = root.val
            self.closestValue(root.left,target)
        return int(self.current)