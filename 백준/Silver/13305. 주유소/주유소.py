import sys
input = sys.stdin.readline
n = int(input().strip())
distance = list(map(int, input().split()))
fees = list(map(int, input().split()))
total_fee = 0

if n == 1:
    print(0)
    sys.exit()

min_fee = min(fees[:-1])

for i,j in enumerate(fees):
    if i == n-1 :
        break
    elif j > min_fee :
        total_fee += distance[i]*j
    else :
        remaining_distance = sum(distance[i:])
        total_fee += remaining_distance * j
        break

print(total_fee)