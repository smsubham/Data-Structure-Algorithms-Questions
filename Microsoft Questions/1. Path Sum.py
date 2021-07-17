
# https://leetcode.com/problems/path-sum/
# https://practice.geeksforgeeks.org/problems/root-to-leaf-path-sum/1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
      
        if root == None:
            return False
    
        if root.left == None and root.right == None and root.val == targetSum:
            return True
        
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
        
        
        
        
        
    #def sumUtility( self, rootm targetSUm)