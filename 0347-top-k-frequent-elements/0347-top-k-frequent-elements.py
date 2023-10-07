class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        common = c.most_common(k)
        answer = []
        for i in common:
            answer.append(i[0])
        return answer