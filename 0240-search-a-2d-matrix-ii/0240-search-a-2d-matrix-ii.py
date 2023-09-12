class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # 문제풀이1: 첫 행의 맨 뒤에서 탐색
#         # 예외 처리
#         if not matrix:
#             return False
    
#         # 첫행의 맨 뒤
#         row = 0
#         col = len(matrix[0]) - 1
        
#         while row <= len(matrix) - 1 and col >= 0:
#             if target == matrix[row][col]:
#                 return True
#             # 타겟이 작으면 왼쪽으로 이동
#             elif target < matrix[row][col]:
#                 col -= 1
#             # 타겟이 크면 아래로 이동
#             elif target > matrix[row][col]:
#                 row += 1
#         return False
    
    # 문제풀이2: 파이썬 다운 풀이
        return any(target in row for row in matrix)