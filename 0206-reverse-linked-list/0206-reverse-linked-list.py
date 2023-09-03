class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next  # 현재 노드의 다음 노드를 임시로 저장
            curr.next = prev       # 현재 노드의 next를 이전 노드로 바꾸기
            prev = curr            # 이전 노드를 현재 노드로 업데이트
            curr = next_node       # 다음 노드로 이동

        return prev




