import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

lo, hi = 0, max(lst)
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2

    total = 0
    for h in lst:
        if h > mid:
            total += h - mid

    if total >= M:        # 더 높여도 M 이상 확보 가능
        ans = mid
        lo = mid + 1      # 경계를 반드시 mid+1로 올림
    else:                 # 부족하면 낮춰야 함
        hi = mid - 1      # hi를 정확히 갱신

print(ans)
