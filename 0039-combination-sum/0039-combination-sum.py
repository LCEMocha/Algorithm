class Solution:
    def combinationSum(self, candidates: List[int], target: int) :
        results = []
        candidates = sorted(candidates)
        
        def dfs(elements, t, start_index):
            if t == 0:
                results.append(elements[:])
                return

            for i in range(start_index, len(candidates)):
                if t >= candidates[i]:
                    elements.append(candidates[i])
                    dfs(elements, t - candidates[i], i)
                    elements.pop()  # Backtrack

        dfs([], target, 0)
        return results               
        