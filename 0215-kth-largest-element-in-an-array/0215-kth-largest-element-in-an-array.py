class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        for _ in range(len(nums)-k):  # k를 빼주는 이유는 k번째 값이 루트가 되어야해서
            heapq.heappop(nums)
        
        return heapq.heappop(nums)
            