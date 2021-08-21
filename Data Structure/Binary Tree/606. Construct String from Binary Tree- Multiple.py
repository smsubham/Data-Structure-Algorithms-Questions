# https://leetcode.com/problems/construct-string-from-binary-tree/
# Source: https://leetcode.com/problems/construct-string-from-binary-tree/discuss/1112030/Python-recursive-solution-with-string-builder
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        sb = [] # init string builder
        
        # helper function to create result
        def helper(node: TreeNode) -> None: 
            if not node:
                return
            
            sb.append(str(node.val))
            
            if not node.left and not node.right:
                # leaf node, stop processing
                return
            
            sb.append('(')          # always wrap left node with parenthesis when right node exist
            helper(node.left)       # process left node recursively 
            sb.append(')')                         

            if node.right:          # adding parenthesis for the right node only if it is not empty
                sb.append('(')
                helper(node.right)
                sb.append(')') 
        
        helper(t)

        return ''.join(sb)

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        sb = [] # init string builder
        
        # helper function to create result
        def helper(node: TreeNode) -> None:
            if not node:
                return
            
            sb.append('(')                      # add 1st wrapping parenthesis
            sb.append(str(node.val))
            
            helper(node.left)                   # process left recursively
            
            if not node.left and node.right:    # add parenthesis if left is empty but right exists
                sb.append('()')
                
            helper(node.right)                  # process right recursively
            
            sb.append(')')                      # add 2nd wrapping parenthesis
        
        helper(t)

        # trim 1st and last parenthesis build result string
        return ''.join(sb[1:-1]) 