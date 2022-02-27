def root_manager(self, nums):
	solutions = []
	len_nums = len(nums)
	
	def subordinate(idx_subproblem, slate):
		solutions.append(list(slate))
		
		for idx_candidate in range(idx_subproblem, len_nums):
			candidate = nums[idx_candidate]
			slate.append(candidate)
			subordinate(idx_candidate + 1, slate) # Careful: next state is not a function of idx_subproblem
			slate.pop()
	
	subordinate(0, [])
	
	return solutions

