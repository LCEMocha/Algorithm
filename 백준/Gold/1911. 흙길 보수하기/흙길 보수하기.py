import sys
input = sys.stdin.readline
N, L = map(int, input().split())
pools = [tuple(map(int, input().split())) for _ in range(N)]
pools.sort()
cover = 0
count = 0
for start, end in pools:
    if cover < start:
        cover = start
    if cover < end:
        needed = (end - cover + L - 1) // L
        count += needed
        cover += needed * L
print(count)