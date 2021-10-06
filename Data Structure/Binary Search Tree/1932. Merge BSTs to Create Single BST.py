#https://leetcode.com/problems/merge-bsts-to-create-single-bst/
#https://leetcode.com/problems/merge-bsts-to-create-single-bst/discuss/1330156/Python-clean-in-order-traversal-solution-O(N)-O(N)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def canMerge(self, trees):
        """
        :type trees: List[TreeNode]
        :rtype: TreeNode
        """
        nodes = {}
        indeg = collections.defaultdict(int)
        for t in trees:
            if t.val not in indeg:
                indeg[t.val] = 0
            if t.left:
                indeg[t.left.val] += 1
                if t.left.val not in nodes: nodes[t.left.val] = t.left
            if t.right:
                indeg[t.right.val] += 1
                if t.right.val not in nodes: nodes[t.right.val] = t.right
            nodes[t.val] = t
            
        # check single root
        sources = [k for k, v in indeg.items() if v == 0]
        if len(sources) != 1: return None
        
        self.cur = float('-inf')
        self.is_invalid = False
        seen = set()
        def inorder(val):
            # check cycle
            if val in seen:
                self.is_invalid = True
                return
            seen.add(val)
            node = nodes[val]
            if node.left: node.left = inorder(node.left.val)
            # check inorder increasing
            if val <= self.cur:
                self.is_invalid = True
                return
            self.cur = val
            if node.right: node.right = inorder(node.right.val)
            return node
        
        root = inorder(sources[0])
        # check full traversal
        if len(seen) != len(nodes) or self.is_invalid:
            return None
        return root