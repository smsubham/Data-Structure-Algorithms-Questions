#https://leetcode.com/problems/find-leaves-of-binary-tree/
#https://zhenyu0519.github.io/2020/03/21/lc336/
class Solution:
	def findLeaves(self, root):
        def dfs(root):
            if not root:
                return -1
            depth = max(dfs(root.left), dfs(root.right))+1
            if depth == len(res):
                res.append([])
            res[depth].append(root.val)
            return depth
        res = []
        dfs(root)
        return res