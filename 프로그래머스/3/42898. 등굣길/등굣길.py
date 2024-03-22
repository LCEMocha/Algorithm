def solution(m, n, puddles):
    matrix = [[0 for i in range(m)] for j in range(n)]
    for x,y in puddles:
        matrix[y-1][x-1] = -1
    matrix[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:  # 물에 잠긴 지역은 건너뜀
                continue
            if i > 0 and matrix[i-1][j] > 0:
                matrix[i][j] += matrix[i-1][j]  # 위쪽에서 오는 경로
            if j > 0 and matrix[i][j-1] > 0:
                matrix[i][j] += matrix[i][j-1]  # 왼쪽에서 오는 경로
            matrix[i][j] %= 1000000007

    return matrix[n-1][m-1]
        