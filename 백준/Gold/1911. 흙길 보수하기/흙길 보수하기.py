N, L = map(int, input().split())
pools = [tuple(map(int, input().split())) for _ in range(N)]

# 1. 웅덩이들을 시작 위치 기준으로 정렬
pools.sort()

cover = 0  # 현재까지 덮은 위치
count = 0  # 사용한 널빤지 개수

for start, end in pools:
    # 현재 덮인 위치보다 웅덩이가 앞에 있으면 갱신
    if cover < start:
        cover = start

    # 이 웅덩이를 덮기 위해 필요한 널빤지 개수 계산
    if cover < end:
        needed = (end - cover + L - 1) // L  # 올림 연산
        count += needed
        cover += needed * L  # 널빤지를 깔아서 덮인 위치 갱신

print(count)