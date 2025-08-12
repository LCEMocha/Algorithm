import sys

input = sys.stdin.readline

L, C = map(int, input().split())
arr = list(map(str, input().split()))

arr.sort()
verb = ['a', 'e', 'i', 'o', 'u']
combinations = []

def backtrack(comb, i, vcnt, ccnt):
    global vc
    if len(comb) == L:
        if vcnt >= 1 and ccnt >= 2:
            combinations.append(''.join(comb))
        return
    for j in range(i, C):
        al = arr[j]
        if len(comb) == L - 1 and vcnt == 0 and al not in verb:
            continue
        if len(comb) == L - 1 and ccnt < 2 and al in verb:
            continue
        nv = vcnt + (1 if al in verb else 0)
        nc = ccnt + (1 if al not in verb else 0)
        comb.append(arr[j])
        backtrack(comb, j + 1, nv, nc)
        comb.pop()

backtrack([], 0, 0, 0)
for i in combinations:
    print(i)