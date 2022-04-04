# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        num_univalue_subtrees = 0
        
        def is_univalue(cur_node):
            nonlocal num_univalue_subtrees
            
            if not cur_node.left and not cur_node.right:
                num_univalue_subtrees += 1                
                return True
            
            is_left_univalue = True
            is_right_univalue = True
            
            if cur_node.left:
                is_left_univalue = is_univalue(cur_node.left) and cur_node.left.val == cur_node.val
                
            if cur_node.right:
                is_right_univalue = is_univalue(cur_node.right) and cur_node.right.val == cur_node.val
                
            is_cur_node_univalue = is_left_univalue and is_right_univalue

            if is_cur_node_univalue:
                num_univalue_subtrees += 1

            return is_cur_node_univalue            
        
        is_univalue(root)
        
        return num_univalue_subtrees
        
            
        
        