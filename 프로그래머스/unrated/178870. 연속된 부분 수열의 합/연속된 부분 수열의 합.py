def solution(sequence, k):
    start, end = 0, 0
    current_sum = sequence[0]
    result = []

    while end < len(sequence):
        if current_sum == k:
            # 현재 부분 수열의 길이를 확인하고, result를 업데이트
            if not result or (end - start) < (result[1] - result[0]):
                result = [start, end]

            # 시작 인덱스를 증가시켜서 다른 부분 수열도 확인
            current_sum -= sequence[start]
            start += 1

        elif current_sum < k:
            end += 1
            if end < len(sequence):
                current_sum += sequence[end]
        else:
            current_sum -= sequence[start]
            start += 1
            if start > end and start < len(sequence):
                end = start
                current_sum = sequence[end]
                
    return result