n = int(input())
ropes = [int(input()) for _ in range(n)]

# 내림차순 정렬
ropes.sort(reverse=True)

# 각 로프를 기준으로 들 수 있는 최대 중량 계산
max_weight = 0
for i in range(n):
    weight = ropes[i] * (i + 1)
    max_weight = max(max_weight, weight)

print(max_weight)
