class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(element, start):
            if sum(element) > target:
                return
            elif sum(element) == target:
                result.append(element[:])
                return
            for i in range(start, len(candidates)):
                element.append(candidates[i])
                dfs(element, i)
                element.pop()
        dfs([],0)
        return result