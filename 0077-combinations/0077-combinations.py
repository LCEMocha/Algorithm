class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(start=1, path=[]):

            if len(path) == k:
                return [path[:]]
            if start > n:
                return []

            with_current = dfs(start + 1, path + [start])

            without_current = dfs(start + 1, path)

            return with_current + without_current

        return dfs()