class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        current_sum = 0
        max_sum = -sys.maxsize
        
        for i in nums:
            current_sum = max(i, current_sum+i)
            max_sum = max(max_sum, current_sum)
        
        return max_sum