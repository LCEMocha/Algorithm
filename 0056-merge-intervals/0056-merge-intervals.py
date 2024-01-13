class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        m = []
        for i in sorted(intervals):
            if m and i[0] <= m[-1][1]:
                m[-1][1] = max(m[-1][1],i[1])
            else:
                # 콤마는 중첩 리스트로 만들어주는 역할을 한다. 그냥 += 만 하면 단순히 요소를 이어붙여줌 
                m += i,
        return m