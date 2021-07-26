# https://leetcode.com/problems/validate-binary-search-tree/

import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.utilValid(root, -sys.maxsize-1, sys.maxsize)
    
    def utilValid(self,root, min, max):
        
        #base case
        if root == None:
            #print("T")
            return True
        #print(min,max,root.val)
        if root.val>min and root.val<max:
            return self.utilValid(root.left,min,root.val) and self.utilValid(root.right,root.val,max)
        
        #print("F", root.val)
        else:
            return False