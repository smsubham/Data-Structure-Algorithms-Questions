# https://leetcode.com/problems/invert-binary-tree/
# Source: https://leetcode.com/problems/invert-binary-tree/discuss/62707/Straightforward-DFS-recursive-iterative-BFS-solutions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        left,right = root.left,root.right
        root.right = self.invertTree(left)
        root.left = self.invertTree(right)
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        stack = []
        stack.append(root)
        
        while len(stack)>0:
            node = stack.pop()
            left = node.left
            node.left = node.right
            node.right = left
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        queue = []
        queue.append(root)
        
        while len(queue)>0:
            node = queue.pop(0)
            left = node.left
            node.left = node.right
            node.right = left
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return root
