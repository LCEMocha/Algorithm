class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 키에 대해 내림차순, 같은 키 내에서는 앞에 서야 할 사람 수에 대해 오름차순으로 정렬
        people.sort(key=lambda x: (-x[0], x[1]))
        
        result = []
        # 정렬된 순서대로 각 사람을 적절한 위치에 삽입
        for person in people:
            result.insert(person[1], person)
        
        return result
        