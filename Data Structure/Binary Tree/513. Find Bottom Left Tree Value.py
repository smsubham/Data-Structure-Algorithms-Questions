#https://leetcode.com/problems/find-bottom-left-tree-value/
#https://leetcode.com/problems/find-bottom-left-tree-value/discuss/98779/Right-to-Left-BFS-(Python-%2B-Java)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        for node in queue:
            queue += filter(None, (node.right, node.left))
        return node.val

