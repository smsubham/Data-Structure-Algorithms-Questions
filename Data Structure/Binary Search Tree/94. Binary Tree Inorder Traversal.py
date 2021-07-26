# https://leetcode.com/problems/binary-tree-inorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.util(root, res)
        return res
    
    def util(self, root, res):
        if root:
            self.util(root.left, res)
            res.append(root.val)
            self.util(root.right, res)