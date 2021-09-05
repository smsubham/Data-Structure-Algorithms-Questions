#https://leetcode.com/problems/binary-tree-tilt/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    tilt =0
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.util(root)
        return self.tilt  
    def util(self,root):
        if root == None:
            return 0
        left = self.util(root.left)
        right = self.util(root.right)
        #print(left,right)
        self.tilt += abs(left-right)
        #print(root.val,self.tilt,left+right+root.val)
        return left+right+root.val