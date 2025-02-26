import sys
#from collections import deque
#import heapq

input = sys.stdin.readline

# n, k = map(int, input().split())
N = int(input().strip())
words = []

for _ in range(N):
    words.append(str(input().strip()))

def is_palindrome(left_point, right_point, w):
    while left_point < right_point and w[left_point] == w[right_point]:
        #print(w, w[left_point], w[right_point])
        left_point += 1
        right_point -= 1
    if left_point == right_point or right_point < left_point:
        return 0
    else:
        return 1, left_point, right_point

for w in words:
    left_point = 0
    right_point = len(w)-1

    result = is_palindrome(left_point, right_point, w)
    if result == 0:
        print(0)
    else:
        if is_palindrome(result[1]+1, result[2], w) == 0 or is_palindrome(result[1], result[2]-1, w) == 0:
            print(1)
        else:
            print(2)