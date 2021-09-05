#https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], val=0) -> int:
        if root == None:
            return 0
        val = 10*val+root.val
        if root.left==None and root.right==None:
            return val
        return self.sumNumbers(root.left,val) +self.sumNumbers(root.right,val) 