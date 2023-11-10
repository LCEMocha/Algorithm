class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp 배열 초기화
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        max_length = 0

        # 동적 프로그래밍을 이용하여 최장 공통 부분 배열의 길이 계산
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    max_length = max(max_length, dp[i][j])

        return max_length        
                        