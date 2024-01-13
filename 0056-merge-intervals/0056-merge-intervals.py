class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        m = []
        s = intervals[0][0]
        e = intervals[0][1]
        for i, j in intervals:
            if s<=i and i<=e:
                if j<e:
                    continue
                e=j
            else:
                m.append([s,e])
                s=i
                e=j
        m.append([s,e])
        return m
                