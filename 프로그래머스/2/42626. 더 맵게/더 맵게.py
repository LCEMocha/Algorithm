import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while len(scoville) > 1:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            return count
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + (min2 * 2)
        heapq.heappush(scoville, new_scoville)
        count += 1
    if scoville[0] >= K:
        return count
    return -1