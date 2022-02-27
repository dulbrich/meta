class Solution:
    def combine(self, nums, k)
        results = []
        
        def rec(idx_subproblem, partial):
            if len(partial) == k:
                results.append(list(partial))
                return
            
            if idx_subproblem == len(nums):
                return
            
            rec(idx_subproblem + 1, partial)
            
            partial.append(idx_subproblem)
            rec(idx_subproblem + 1, partial)
            partial.pop()
            
        rec(0, [])
        
        return results