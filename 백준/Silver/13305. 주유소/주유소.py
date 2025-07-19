import sys
input = sys.stdin.readline
n = int(input().strip())
distance = list(map(int, input().split()))
fees = list(map(int, input().split()))
total_fee = 0
min_fee = min(fees[:-1])

p = 0
while p < n-1:
    if fees[p] == min_fee:
        remaining_distance = sum(distance[p:])
        total_fee += remaining_distance * fees[p]
        break
    elif fees[p] < fees[p + 1]:
        next_p = p + 1
        total_fee += distance[p] * fees[p]
        while fees[p] < fees[next_p] and next_p < n-1:
            total_fee += distance[next_p] * fees[p]
            next_p += 1
        p = next_p
    else:
        total_fee += distance[p] * fees[p]
        p += 1

print(total_fee)