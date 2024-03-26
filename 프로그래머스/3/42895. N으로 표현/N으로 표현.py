def solution(N, number):
    if N == number:
        return 1

    # 1부터 8까지의 사용 횟수로 만들 수 있는 숫자들의 집합을 저장할 리스트
    # dp[i]는 N을 i+1번 사용해서 만들 수 있는 숫자들의 집합
    dp = [set() for _ in range(8)]
    
    for i in range(8):
        dp[i].add(int((str(N)*(i+1))))

        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i-j-1]:
                    dp[i].add(op1+op2)
                    dp[i].add(op1-op2)
                    dp[i].add(op1*op2)
                    if op1 != 0 and op2 !=0:
                        dp[i].add(op1//op2)
        if number in dp[i]:
            return i+1

    return -1