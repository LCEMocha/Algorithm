class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = list(jewels)
        answer = 0
        for i in s:
            answer += stones.count(i)
        return answer