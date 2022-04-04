class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        found_sum = False
        
        if not root:
            return found_sum
        
        def top_down_dfs(cur_node, cur_sum):
            nonlocal found_sum
            
            if not cur_node.left and not cur_node.right:
                if cur_sum + cur_node.val == targetSum:
                    found_sum = True
            
            if cur_node.left and not found_sum:
                top_down_dfs(cur_node.left, cur_sum + cur_node.val)
            
            if cur_node.right and not found_sum:
                top_down_dfs(cur_node.right, cur_sum + cur_node.val)
        
        top_down_dfs(root, 0)
        
        return found_sum