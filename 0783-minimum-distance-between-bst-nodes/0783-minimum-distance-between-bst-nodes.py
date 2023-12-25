# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.minus = float('inf')
        self.prev = None  # 이전 노드를 저장할 변수

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:  # 이전 노드가 존재하면 차이 계산
                self.minus = min(self.minus, node.val - self.prev.val)
            self.prev = node  # 현재 노드를 이전 노드로 업데이트
            inorder(node.right)

        inorder(root)
        return self.minus
