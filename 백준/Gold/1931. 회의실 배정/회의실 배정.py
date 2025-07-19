import sys
input = sys.stdin.readline

n = int(input().strip())
times = [list(map(int, input().split())) for _ in range(n)]

# 종료 시간 우선으로 정렬
times.sort(key=lambda x: (x[1], x[0]))

end_time = 0
count = 0

for start, end in times:
    if start >= end_time:
        count += 1
        end_time = end

print(count)
