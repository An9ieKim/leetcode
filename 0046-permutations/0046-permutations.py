class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    ### 문제풀이 1: DFS를 활용한 순열 생성
#         results = []
#         prev_elements = []
        
#         def dfs(elements):
#             # 리프 노드일 때 결과 추가
#             if len(elements) == 0:
#                 results.append(prev_elements[:])
            
#             # 순열 생성 재귀 호출
#             for e in elements:
#                 next_elements = elements[:]
#                 next_elements.remove(e)
                
#                 prev_elements.append(e)
#                 dfs(next_elements)
#                 prev_elements.pop()
                
#         dfs(nums)
#         return results
    
    ### 문제풀이 2: itertools 모듈 활용
        return list(itertools.permutations(nums))