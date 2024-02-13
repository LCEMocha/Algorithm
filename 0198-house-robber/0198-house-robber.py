class Solution:
    def rob(self, nums: List[int]) -> int:
        # 집이 없는 경우
        if not nums:
            return 0
        
        # 집이 하나뿐인 경우
        if len(nums) == 1:
            return nums[0]
        
        # 타뷸레이션 테이블 초기화
        dp = [0] * len(nums)
        
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
        