#https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
#Source: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/discuss/270025/JavaC%2B%2BPython-Recursive-Solution
"""
Intuition
Easily decompose this problem into 2 sub-problem:

Find all path from root to leaves. DFS recursion should help do that.
Transform a path from base to base 10.
You can do this separately, and it will be a O(N^2) solution.
In my solution, I combine them together.

Explanation:
We recursively pass the current value of path to the children.
If root == null, no value, return 0.
If root != null,
we double the value from its parent and add the node's value,
like the process of transforming base 2 to base 10.

In the end of recursion,
if root.left == root.right == null,
return the current val.

Complexity:
Time O(N)
Space O(H) for recursion.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode],val=0) -> int:
        if not root: return 0
        val = val * 2 + root.val
        if root.left == root.right: return val
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)