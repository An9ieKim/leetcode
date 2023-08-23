# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    ### 문제풀이 1: 재귀구조 DFS로 브루트 포스 탐색
#         if not root:
#             return 0
        
#         return (root.val if low <= root.val <= high else 0) + \
#                 self.rangeSumBST(root.left, low, high) + \
#                 self.rangeSumBST(root.right, low, high)
    
    ### 문제풀이 2: DFS 가지치기로 필요한 노드 탐색
#         def dfs(node: TreeNode):
#             if not node:
#                 return 0
            
#             if node.val < low:
#                 return dfs(node.right)
#             elif node.val > high:
#                 return dfs(node.left)
#             return node.val + dfs(node.left) + dfs(node.right)

#         return dfs(root)
    
    ### 문제풀이 3: 반복 구조 DFS로 필요한 노드 탐색
#         stack, sum = [root], 0
#         # 스택 이용 필요한 노드 DFS 반복
#         while stack:
#             node = stack.pop()
#             if node:
#                 if node.val > low:
#                     stack.append(node.left)
#                 if node.val < high:
#                     stack.append(node.right)
#                 if low <= node.val <= high:
#                     sum += node.val
#         return sum
    
    ### 문제풀이 4: 반복 구조 BFS로 필요한 노드 탐색
        stack, sum = [root], 0
        # 큐 연산을 이용해 반복 구조 BFS로 필요한 노드 탐색
        while stack:
            node = stack.pop(0)
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum