import sys
input = sys.stdin.readline
#n = int(input().strip())
distance = list(map(int, input().split()))

x, y = distance[0], distance[1]
w, s = distance[2], distance[3]

if s >= 2 * w :
    result = (x+y) * w
else :
    if s >= w:
        result = min(x, y)*s + abs(x-y)*w
    else:
        diff = abs(x-y)
        same = min(x, y)
        if diff % 2 == 0:
            result = same*s + diff*s
        else:
            result = same*s + (diff-1)*s + w

print(result)