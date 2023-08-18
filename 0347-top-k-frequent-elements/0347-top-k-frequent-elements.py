class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
    ### 문제풀이 1: Counter를 이용한 음수 순 추출
#         freqs = collections.Counter(nums)
#         freqs_heap = []
#         # 힙에 음수로 삽입
#         for f in freqs:
#             heapq.heappush(freqs_heap, (-freqs[f], f))
                                         
#         topk = list()
#         # k번만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출
#         for _ in range(k):
#             topk.append(heapq.heappop(freqs_heap)[1])
                                    
#         return topk
        
    
    ### 문제풀이 2: 파이썬다운 방식
        return list(zip(*collections.Counter(nums).most_common(k)))[0]