import sys
from math import isqrt

input = sys.stdin.readline

N, L = map(int, input().split())
jobs = []  # (deadline d, reward c)

for _ in range(N):
    x, y, c = map(int, input().split())
    s = x*x + y*y  # squared distance
    r_floor = isqrt(s)
    # ceil(sqrt(s)) via integer arithmetic
    r_ceil = r_floor if r_floor*r_floor == s else r_floor + 1
    d = L - r_ceil
    if d >= 0:
        jobs.append((d, c))

# 마감 기한 오름차순으로 정렬
jobs.sort(key=lambda t: t[0])

import heapq
heap = []  # 선택된 보상들의 최소 힙
for d, c in jobs:
    heapq.heappush(heap, c)
    # 시간 0..d까지는 총 d+1개까지만 배치 가능
    if len(heap) > d + 1:
        heapq.heappop(heap)  # 가장 작은 보상은 버린다

print(sum(heap))