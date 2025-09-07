import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = deque([0] * w)  # 다리 위 상태(길이 w)
load = 0  # 현재 다리 하중
time = 0
i = 0 

while n > i :
    time += 1
    load -= bridge.popleft()
    
    if load + trucks[i] <= L:
        bridge.append(trucks[i])
        load += trucks[i]
        i += 1
    else:
        bridge.append(0)

time += w
print(time)