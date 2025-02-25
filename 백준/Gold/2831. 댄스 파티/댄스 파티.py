def max_couples(men, women):
    men_pos = sorted([m for m in men if m > 0])
    men_neg = sorted([-m for m in men if m < 0])
    women_pos = sorted([w for w in women if w > 0])
    women_neg = sorted([-w for w in women if w < 0])

    def count_pairs(men_list, women_list):
        count = 0
        i, j = 0, 0
        while i < len(men_list) and j < len(women_list):
            if men_list[i] < women_list[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count

    count1 = count_pairs(men_pos, women_neg)
    count2 = count_pairs(women_pos, men_neg)

    return count1 + count2

# 입력 예시
n = int(input())
men = list(map(int, input().split()))
women = list(map(int, input().split()))

# 결과 출력
print(max_couples(men, women))
