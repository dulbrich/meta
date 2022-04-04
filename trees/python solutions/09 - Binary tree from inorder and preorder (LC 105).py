class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = {}
        
        for idx, value in enumerate(inorder):
            inorder_indices[value] = idx
        
        def get_subtree(start_pre, end_pre, start_ino, end_ino):
            if start_pre > end_pre:
                return None
            
            cur_root_val = preorder[start_pre]
            cur_root_inorder_pos = inorder_indices[cur_root_val]
            
            cur_root = TreeNode(cur_root_val)        
            
            left_size = cur_root_inorder_pos - start_ino
            cur_root.left = get_subtree(start_pre + 1, start_pre + left_size, start_ino, cur_root_inorder_pos - 1)
            
            right_size = end_ino - cur_root_inorder_pos
            cur_root.right = get_subtree(start_pre + left_size + 1, end_pre, cur_root_inorder_pos + 1, end_ino)
                        
            return cur_root
            
            
        return get_subtree(0, len(preorder) - 1, 0 , len(inorder) - 1)