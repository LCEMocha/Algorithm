import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = list(map(int, input().split()))

lo, hi = 1, max(arr)
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2  # 후보 길이 L
    cnt = 0
    for a in arr:
        cnt += a // mid
    if cnt >= M:          # 이 길이로 M명 이상 줄 수 있으면 더 키워본다
        ans = mid
        lo = mid + 1
    else:                 # 못 주면 길이를 줄인다
        hi = mid - 1

print(ans)