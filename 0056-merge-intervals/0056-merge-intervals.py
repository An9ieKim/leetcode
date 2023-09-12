class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    # 정렬하여 병합
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,

        return merged