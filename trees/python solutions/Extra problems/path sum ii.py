def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:     
	solutions = []
	
	if not root:
		return solutions
	
	def top_down_dfs(cur_node, cur_sum, cur_path):
		cur_path.append(cur_node.val)
		
		if not cur_node.left and not cur_node.right:
			if cur_sum + cur_node.val == targetSum:              
				solutions.append(cur_path[:])
		
		if cur_node.left:
			top_down_dfs(cur_node.left, cur_sum + cur_node.val, cur_path)
		
		if cur_node.right:
			top_down_dfs(cur_node.right, cur_sum + cur_node.val, cur_path)
		
		cur_path.pop()
	
	top_down_dfs(root, 0, [])
	
	return solutions