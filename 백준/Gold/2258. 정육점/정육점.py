import sys
input = sys.stdin.readline

n, m = map(int, input().split())
meat_charge = [list(map(int, input().split())) for _ in range(n)]

# 가격을 기준으로 정렬 (같은 가격이면 무게가 큰 순으로 정렬)
meat_charge.sort(key=lambda x: (x[1], -x[0]))

total_weight = 0
total_cost = 0
prev_price = -1
min_charge = float('inf')

def check_cheapest(min_charge, meat_charge, current_price, i, n):
    """ 더 싼 가격에서 필요한 고기를 얻을 수 있는지 확인 """
    while i < n - 1 and meat_charge[i][1] == current_price:
        i += 1
    if i < n and current_price < meat_charge[i][1] < min_charge:
        return meat_charge[i][1]
    return min_charge

for i in range(n):
    weight, price = meat_charge[i]
    total_weight += weight

    # 같은 가격이면 중복 누적을 방지 (한 번만 더하기)
    if price != prev_price:
        total_cost = price
    else:
        total_cost += price

    prev_price = price

    if total_weight >= m:
        min_charge = min(min_charge, total_cost)
        min_charge = check_cheapest(min_charge, meat_charge, price, i, n)
        break  # 최소 비용을 찾으면 더 이상 탐색할 필요 없음

print(min_charge if total_weight >= m else -1)
