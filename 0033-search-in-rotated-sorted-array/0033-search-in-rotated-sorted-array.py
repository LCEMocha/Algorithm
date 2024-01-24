class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 왼쪽 부분이 정렬되어 있는 경우
            if nums[left] <= nums[mid]:
                # 타겟이 왼쪽 부분에 있는 경우
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:  # 타겟이 오른쪽 부분에 있는 경우
                    left = mid + 1
            else:  # 오른쪽 부분이 정렬되어 있는 경우
                # 타겟이 오른쪽 부분에 있는 경우
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:  # 타겟이 왼쪽 부분에 있는 경우
                    right = mid - 1

        return -1