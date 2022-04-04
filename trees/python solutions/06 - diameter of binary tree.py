class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_diameter = 0
        
        def get_height(cur_node):
            nonlocal max_diameter
            
            if not cur_node.left and not cur_node.right:
                return 0
            
            left_height = 0
            right_height = 0
            
            if cur_node.left:
                left_height = 1 + get_height(cur_node.left)
            
            if cur_node.right:
                right_height = 1 + get_height(cur_node.right)
                
            my_diameter = left_height + right_height
            max_diameter = max(max_diameter, my_diameter)    
                
            return max(left_height, right_height)
                
        get_height(root)
        
        return max_diameter