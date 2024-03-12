def solution(word):
    # 모음 순서와 각 모음이 나올 때마다 더해지는 순서 값
    vowels = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = 0
    # 각 자리수마다 가능한 조합의 수
    pattern = [781, 156, 31, 6, 1]
    
    for i, char in enumerate(word):
        # 해당 모음의 순서 * 해당 위치에서의 조합 수 + 1(자기 자신을 포함)
        answer += vowels[char] * pattern[i] + 1
    return answer
