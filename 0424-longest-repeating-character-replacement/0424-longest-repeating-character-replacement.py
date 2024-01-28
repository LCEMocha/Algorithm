class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()  # 문자의 출현 횟수를 저장할 Counter
        most_frequent = 0
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            count[char] += 1  # 현재 문자의 출현 횟수를 1 증가
            most_frequent = max(most_frequent, count[char])

             # (윈도우 크기 - most_frequent의 출현 횟수 > k)인 경우 (즉, 변경 가능한 횟수를 초과한 경우)
            if (right - left + 1) - most_frequent > k:
                count[s[left]] -= 1  # 포인터가 옮겨가기 위해 현 left의 문자 횟수 1 차감
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len