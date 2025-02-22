import sys
input = sys.stdin.readline

n, k = map(int, input().split())
heights = list(map(int, input().split()))

# 인접한 키 차이 계산
differences = [heights[i+1] - heights[i] for i in range(n-1)]

# 키 차이를 오름차순으로 정렬
differences.sort()

# 전체 불편함 최소화: 가장 큰 (K - 1)개의 차이를 제거
result = sum(differences[:n - k])

# 결과 출력
print(result)