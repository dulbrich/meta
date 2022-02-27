class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        def rec(sub, partial):
            if len(nums) == sub:
                results.append(list(partial))
                return
            
            rec(sub + 1, partial)
            
            partial.append(nums[sub])
            rec(sub + 1, partial)
            partial.pop()
            
        rec(0, [])
        
        return results