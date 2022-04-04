class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        def get_next_subtree_root(start_idx, end_idx):
            if start_idx > end_idx: # think about [0,1] test case
                return None
            
            if start_idx == end_idx:
                return TreeNode(nums[start_idx])
            
            root_idx = (start_idx + end_idx) // 2
            cur_node = TreeNode(nums[root_idx])
            cur_node.left = get_next_subtree_root(start_idx, root_idx - 1)
            cur_node.right = get_next_subtree_root(root_idx + 1, end_idx)
            
            return cur_node
                  
        return get_next_subtree_root(0, len(nums) - 1)

