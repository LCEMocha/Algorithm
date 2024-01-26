class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if not nums or k == 0:
            return []

        dq = deque()
        result = []

        for i, num in enumerate(nums):
            # 윈도우의 왼쪽 끝이 큐의 첫 번째 요소보다 커지면 해당 요소를 제거
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # 현재 요소가 큐의 마지막 요소보다 크거나 같을 때까지 큐의 마지막 요소 제거
            while dq and nums[dq[-1]] <= num:
                dq.pop()

            # 현재 인덱스 추가
            dq.append(i)

            # 윈도우의 크기가 k가 되면, 최대값 추가
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

