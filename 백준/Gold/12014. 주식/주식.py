import sys
input = sys.stdin.readline
import bisect
T = int(input().strip())
for t in range(T):
    N, k = map(int, input().split())
    n = list(map(int, input().split()))

    def lis(n, k):
        dp = []
        for i in n:
            idx = bisect.bisect_left(dp, i)
            if idx == len(dp):
                dp.append(i)
                k -= 1
                if k == 0:
                    return 1
            else:
                dp[idx] = i

    print("Case #" + str(t + 1))
    print(1 if lis(n,k) == 1 else 0)