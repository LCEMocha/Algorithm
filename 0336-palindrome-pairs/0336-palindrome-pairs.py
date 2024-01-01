class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)  # 자식 노드들을 저장할 딕셔너리
        self.word_id = -1  # 단어의 인덱스를 저장, 초기값은 -1
        self.palindrome_word_ids = []  # 현재 노드에서 끝나는 서브워드 중 팰린드롬인 단어의 인덱스 목록

class Trie:
    def __init__(self):
        self.root = TrieNode()  # 트라이의 루트 노드
    
    @staticmethod
    def is_palindrome(word):
        # 주어진 단어가 팰린드롬인지 확인하는 함수
        return word == word[::-1]
    
    # 단어를 트라이에 삽입하는 함수
    def insert(self, index, word):
        node = self.root
        for i, char in enumerate(reversed(word)):
            # 단어의 일부가 팰린드롬인 경우 해당 인덱스를 palindrome_word_ids에 추가
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            # 현재 문자에 해당하는 자식 노드로 이동
            node = node.children[char]
        node.word_id = index  # 단어의 마지막 문자에 단어 인덱스 저장
    
    # 특정 단어에 대해 팰린드롬 쌍을 찾는 함수
    def search(self, index, word):
        result = []
        node = self.root
        
        while word:
            # 현재 노드가 단어의 끝이고, 남은 부분이 팰린드롬인 경우
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            # 현재 문자가 자식 노드에 없는 경우 탐색 종료
            if word[0] not in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]
        
        # 단어 전체를 탐색한 후, 현재 노드가 다른 단어의 끝인 경우
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
        # 현재 노드에서 끝나는 서브워드 중 팰린드롬인 단어들 추가
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        
        # 모든 단어를 트라이에 삽입
        for i, word in enumerate(words):
            trie.insert(i, word)
            
        results = []
        # 각 단어에 대해 팰린드롬 쌍 검색
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))
        return results  # 찾은 팰린드롬 쌍 반환
