import sys
input = sys.stdin.readline

n, m = map(int, input().split())
meat_charge = []
for _ in range(n):
    meat_charge.append(list(map(int, input().split())))

meat_charge.sort(key = lambda x : (x[1], -x[0]))

charges = []
min_charge = 0

def check_cheapest(min_charge, meat_charge, current_charge, i, n):
    while i < n-1 and current_charge == meat_charge[i][1]:
        i += 1
    if current_charge < meat_charge[i][1] < min_charge:
        return meat_charge[i][1]
    return min_charge

for i in range(n):
    m -= meat_charge[i][0]
    charges.append(meat_charge[i][1])
    if m <= 0 :
        l = len(charges)
        if l <= 1:
            min_charge = charges[-1]
        elif charges[-1] == charges[-2]:
            idx = -1
            while idx > -l and charges[idx] == charges[idx-1]:
                min_charge += charges[idx]
                idx -= 1
            min_charge += charges[idx]
        else:
            min_charge = charges[-1]

        #print(meat_charge, charges, min_charge)
        min_charge = check_cheapest(min_charge, meat_charge, charges[-1], i, n)
        break

if m > 0:
    print(-1)
else:
    print(min_charge)