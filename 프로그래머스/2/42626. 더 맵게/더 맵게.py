import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while len(scoville)>1:
        m1 = heapq.heappop(scoville)
        if m1 >= K:
            return count
        m2 = heapq.heappop(scoville)
        new = m1 + (m2*2)
        heapq.heappush(scoville, new) 
        count += 1
    if heapq.heappop(scoville) >= K:
        return count
    return -1
    
    