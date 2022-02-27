class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        
        def rec(sub, partial):
            if len(partial) == k:
                results.append(list(partial))
                return
            
            if n + 1 == sub:
                return
            
            rec(sub + 1, partial)
            
            partial.append(sub)
            rec(sub + 1, partial)
            partial.pop()
            
        rec(1, [])
        
        return results