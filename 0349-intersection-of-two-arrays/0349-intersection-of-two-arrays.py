class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        result = []
        [result.append(x) for x in nums1 if x in nums2]
        return result
