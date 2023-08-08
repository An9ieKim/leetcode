class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
    
    ### 문제풀이 1: 오름차순 풀이
#         sum = 0
#         pair = []
#         nums.sort()
        
#         for n in nums:
#         # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
#             pair.append(n)
#             if len(pair) == 2:
#                 sum += min(pair)
#                 pair = []
                
#         return sum
    
    ### 문제풀이 2: 짝수번째 값 계산
#         sum = 0
#         nums.sort()
        
#         for i, n in enumerate(nums):
#             # 짝수번째 값의 합 계산
#             if i % 2 == 0:
#                 sum += n
                
#         return sum
    
    ### 문제풀이 3: 파이썬다운 방식
        return sum(sorted(nums)[::2])