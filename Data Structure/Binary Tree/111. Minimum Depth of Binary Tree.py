#https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Edge cases: [2,null,3,null,4,null,5,null,6]> 5
#We need to add the smaller one of the child depths - except if that's zero, then add the larger one. The first Python solution is the clearest because it lets me directly say exactly that.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        d, D = sorted(map(self.minDepth, (root.left, root.right)))
        return 1 + (d or D)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
def minDepth(self, root):
    if not root: return 0
    d = map(self.minDepth, (root.left, root.right))
    return 1 + (min(d) or max(d))