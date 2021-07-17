# https://leetcode.com/problems/path-sum-ii/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    # 2:32
    def pathSum(self, root, sum):
        output = []
        self.findPathSum(root, sum, [], output)

        return output

    def findPathSum(self, root, sum, temp, output):
        if not root:
            return

        if not root.left and not root.right and sum == root.val:
            temp.append(root.val)
            print(root.val)
            print("Temp: ",temp)
            output.append(temp[:])
            print("Output: ",output)
            return

        sum -= root.val
        temp.append(root.val)
        self.findPathSum(root.left, sum, temp[:], output)
        self.findPathSum(root.right, sum, temp[:], output)
