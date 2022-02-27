def lcp(input_str):
	solutions = []
	len_input = len(input_str)
	
	def fill_blanks(idx_subproblem, slate):
		# Base case
		if idx_subproblem == len_input:
			solutions.append("".join(slate))
			return
		
		# Recursive case
		if input_str[idx_problem].isdigit():
			slate.append(input_str[idx_subproblem])
			fill_blanks(idx_subproblem + 1, slate)
			slate.pop()
		else:
			slate.append(input_str[idx_subproblem].lower())
			fill_blanks(idx_subproblem + 1, slate)
			slate.pop()
			
			slate.append(input_str[idx_subproblem].upper())
			fill_blanks(idx_subproblem + 1, slate)
			slate.pop()
				
	fill_blanks(0, []) # Root manager call
	
	return solutions
	