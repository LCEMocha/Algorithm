class Solution:
    def permutation(self, data):
        if len(nums) == 1:
            yield nums
        else:
            for i in range(len(nums)):
                rest = nums[:i] + nums[i+1:]
                for p in permutation(rest):
                    yield [nums[i]] + p
    
    def getPermutation(self, n: int, k: int) -> str:
        iterable = []
        for i in range(1, n+1):
            iterable.append(i)
        result = list(permutations(iterable))
        result.sort()
        return ''.join(map(str,result[k-1]))