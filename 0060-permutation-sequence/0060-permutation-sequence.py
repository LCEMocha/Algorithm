class Solution:
    def permutation(self, data):
        n = len(data)
        c = [0] * n
        yield data[:]

        i = 0
        while i < n:
            if c[i] < i:
                if i % 2 == 0:
                    data[0], data[i] = data[i], data[0]
                else:
                    data[c[i]], data[i] = data[i], data[c[i]]
                yield data[:]
                c[i] += 1
                i = 0
            else:
                c[i] = 0
                i += 1
    
    def getPermutation(self, n: int, k: int) -> str:
        iterable = []
        for i in range(1, n+1):
            iterable.append(i)
        result = []
        for p in permutations(iterable):
            result.append(p)
        result.sort()
        return ''.join(map(str,result[k-1]))
    
