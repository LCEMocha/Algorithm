from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(self.combi(range(1,n+1), k))
        
    def combi(self, iterable, r):
        pool = tuple(iterable)
        l = len(pool)

        if r > l:
            return

        indices = list(range(r))
        yield tuple(pool[i] for i in indices)

        while True:
            for i in reversed(range(r)):
                if indices[i] != i + l - r:
                    break
            else:
                return

            indices[i] += 1
            for j in range(i + 1, r):
                indices[j] = indices[j-1] + 1

            yield tuple(pool[i] for i in indices)
