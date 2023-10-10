from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        li = []
        for i in range(n):
            li.append(i+1)
        result = list(permutations(li,n))
        return ''.join(map(str,result[k-1]))