class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    
    ### 문제풀이1: heqpq 모듈 이용
#         heap = list()
#         for n in nums:
#             heapq.heappush(heap, -n)
            
#         for _ in range(1, k):
#             heapq.heappop(heap)
            
#         return -heapq.heappop(heap)
    
    ### 문제풀이2: heapq 모듈의 heapify 이용
#         heapq.heapify(nums)
        
#         for _ in range(len(nums) - k):
#             heapq.heappop(nums)
            
#         return heapq.heappop(nums)
    
    ### 문제풀이3: heapq 모듈의 nlargest 이용
#         return heapq.nlargest(k, nums)[-1]
    
    ### 문제풀이4: 정렬을 이용한 풀이
        return sorted(nums, reverse=True)[k - 1]