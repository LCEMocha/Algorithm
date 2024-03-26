from collections import deque

def can_transform(word1, word2):
    # 한 번에 하나의 문자만 다를 때 변환이 가능하다고 판단
    diff_count = sum([word1[i] != word2[i] for i in range(len(word1))])
    return diff_count == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)]) # (현재 단어, 변환 횟수)
    visited = set([begin])
    
    while queue:
        current_word, count = queue.popleft()
        
        if current_word == target:
            return count
        
        for word in words:
            if word not in visited and can_transform(current_word, word):
                visited.add(word)
                queue.append((word, count + 1))
    
    return 0
    