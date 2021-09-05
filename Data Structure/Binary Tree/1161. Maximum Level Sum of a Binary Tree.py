#https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxValue,level,maxLevel = -float('inf'),0,0
        queue = collections.deque()
        queue.append(root)
        while queue:
            level +=1
            currentLevelSum =0
            for _ in range(len(queue)):
                node = queue.popleft()
                currentLevelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if maxValue < currentLevelSum:
                maxValue,maxLevel = currentLevelSum, level
        return maxLevel