class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    # 문제풀이: 유클리스 거리의 우선순위 큐 순서
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))
            
        result = []
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result