import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def div_toward_zero(a, b):
    # 파이썬 // 는 음수에서 내림이므로, 0을 향해 버림이 되도록 보정
    if a >= 0:
        return a // b
    else:
        return -((-a) // b)

def main():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    plus, minus, mul, div_ = map(int, input().split())

    max_val = -10**18
    min_val =  10**18

    def dfs(idx, acc, p, m, mu, d):
        nonlocal max_val, min_val
        if idx == n:
            if acc > max_val: max_val = acc
            if acc < min_val: min_val = acc
            return

        x = nums[idx]
        if p:
            dfs(idx + 1, acc + x, p - 1, m, mu, d)
        if m:
            dfs(idx + 1, acc - x, p, m - 1, mu, d)
        if mu:
            dfs(idx + 1, acc * x, p, m, mu - 1, d)
        if d:
            dfs(idx + 1, div_toward_zero(acc, x), p, m, mu, d - 1)

    dfs(1, nums[0], plus, minus, mul, div_)
    print(max_val)
    print(min_val)

if __name__ == "__main__":
    main()
