class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        c = []
        answer = []
        for i,j in points:
            c.append(abs(i)**2+abs(j)**2)
        c = list(enumerate(c))
        c = sorted(c, key=lambda x: x[1])
        for i,j in c:
            if (k-1)>=0:
                answer.append(points[i])
                k -= 1
        return answer