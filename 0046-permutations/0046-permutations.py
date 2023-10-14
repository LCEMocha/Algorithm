
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
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        for p in self.permutation(nums):
            result.append(p)
        result.sort()
        return result