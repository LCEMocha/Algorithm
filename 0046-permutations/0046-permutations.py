class Solution:        
    def permutation(self, data):
        if len(data) == 1:
            yield data
        else:
            for i in range(len(data)):
                rest = data[:i] + data[i + 1:]
                for p in self.permutation(rest):
                    yield [data[i]] + p
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list(self.permutation(nums))
        result.sort()
        return result