import sys
input = sys.stdin.readline

#n, k = map(int, input().split())
nums = []
sums = 0
N = int(input().strip())
n = N

for _ in range(n):
    nums.append(int(input().strip()))

nums.sort()

# 음수처리
i = 0
while i+1 <= (n-1) and nums[i+1] <= 0:
    sums += (nums[i] * nums[i+1])
    i += 2

# 1보다 큰 양수처리
n -= 1
while (n-1 > i) and (nums[n] != 1) and (nums[n-1] != 1):
    sums += (nums[n] * nums[n-1])
    n -= 2

# 1 처리
if nums[n-1] == 1:
    while n > i and nums[n-1] == 1:
        sums += nums[n]
        n -= 1

if (i != n) and (i <= N-1) and (nums[i] <= 0):
    sums += (nums[i] + nums[n])
elif (i != n) and (i <= N-1) and nums[i] > 0:
    sums += (nums[n] * nums[n-1])
else:
    sums += nums[n]

print(sums)