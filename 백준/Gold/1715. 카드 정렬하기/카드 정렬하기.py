import sys
from collections import deque
import heapq

input = sys.stdin.readline

# n, k = map(int, input().split())
N = int(input().strip())
cards = []

for _ in range(N):
    heapq.heappush(cards, int(input().strip()))

answer = 0
while cards:
    a = heapq.heappop(cards)
    if cards:
        b = heapq.heappop(cards)
        heapq.heappush(cards, a+b)
        answer += (a+b)
    else:
        break

print(answer)