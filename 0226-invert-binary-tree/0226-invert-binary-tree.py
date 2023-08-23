# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    ### 문제풀이 1: 파이썬다운 방식
#         if root:
#             root.left, root.right = \
#                 self.invertTree(root.right), self.invertTree(root.left)
#             return root
    
    ### 문제풀이 2: 반복구조로 BFS
#         queue = collections.deque([root])
        
#         while queue:
#             node = queue.popleft()
#             # 부모 노드부터 하향식 스왑
#             if node:
#                 node.left, node.right = node.right, node.left
                
#                 queue.append(node.left)
#                 queue.append(node.right)
#         return root
    
    ### 문제풀이 3: 반복구조로 DFS
#         stack = collections.deque([root])
        
#         while stack:
#             node = stack.pop()
#             # 부모 노드부터 하향식 스왑
#             if node:
#                 node.left, node.right = node.right, node.left
                
#                 stack.append(node.left)
#                 stack.append(node.right)
#         return root
    
    ### 문제풀이 4: 반복구조로 DFS 후위 순회
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()
            
            if node:
                stack.append(node.left)
                stack.append(node.right)
        
                node.left, node.right = node.right, node.left # 후위 순회
            
        return root