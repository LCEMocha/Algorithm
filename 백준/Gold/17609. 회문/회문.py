import sys
input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    w = str(input().strip())
    left_point = 0
    right_point = len(w) - 1

    def is_palindrome(left_point, right_point, w):
        while left_point < right_point and w[left_point] == w[right_point]:
            left_point += 1
            right_point -= 1
        if left_point == right_point or right_point < left_point:
            return 0
        else:
            return 1, left_point, right_point

    result = is_palindrome(left_point, right_point, w)
    if result == 0:
        print(0)
    else:
        if is_palindrome(result[1]+1, result[2], w) == 0 or is_palindrome(result[1], result[2]-1, w) == 0:
            print(1)
        else:
            print(2)