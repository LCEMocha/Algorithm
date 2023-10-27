class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(elements, start, k):
            if k == 0:
                result.append(elements[:])
                return

            for i in range(start, len(nums)):
                elements.append(nums[i])  # 트리에서 깊어지는 부분
                dfs(elements, i+1, k-1)
                elements.pop()  # 트리에서 거꾸로 올라오는 부분

                
        for i in range(len(nums)+1):
            dfs([], 0, i)
        return result
