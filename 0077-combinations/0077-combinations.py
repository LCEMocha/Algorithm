from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        li = []
        for i in range(1,n+1):
            li.append(i)
        result = list(combinations(li,k))
        return result