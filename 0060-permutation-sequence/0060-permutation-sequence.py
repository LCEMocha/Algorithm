class Solution:
    def permutation(self, data):
        if len(data) == 1:
            yield data
        else:
            for i in range(len(data)):
                rest = data[:i] + data[i+1:]
                for p in self.permutation(rest):
                    yield [data[i]] + p
    
    def getPermutation(self, n: int, k: int) -> str:
        iterable = []
        for i in range(1, n+1):
            iterable.append(i)
        result = list(permutations(iterable))
        result.sort()
        return ''.join(map(str,result[k-1]))