# Faster than 98% | Recursive |
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def findCombinations(candidates, target, curr, res):
            if target == 0:
                res.append(curr); return  # Base Condition 1 (Feasible Solution Found)
            for i, candidate in enumerate(candidates):
                if target-candidate < 0: break  # Base Condition 2 (No Feasible Solutions)
                if i !=0 and candidates[i]==candidates[i-1]: continue  # Ignore multiple copies
                findCombinations(candidates[i+1:], target-candidate, curr+[candidate], res)  # Recurse       
        res = []  # initialise solution set to be empty...
        candidates.sort()  # Sort first as easier to find distinct solutions later...
        findCombinations(candidates, target, [], res)
        return res