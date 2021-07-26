# https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Credit: https://leetcode.com/problems/find-mode-in-binary-search-tree/discuss/780598/Easy-Recursive-Python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        cnts = collections.Counter()
        maxValue = 0
        def helper(node):
            nonlocal maxValue
            if not node:
                return
            cnts[node.val] += 1
            maxValue = max(maxValue, cnts[node.val])
            helper(node.left)
            helper(node.right)
            
        helper(root)
        return [k for k,v in cnts.items() if v == maxValue]