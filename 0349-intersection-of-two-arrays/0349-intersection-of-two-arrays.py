class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
    # 문제풀이1: 브루트포스로 계산
#         result: Set = set()
#         for n1 in nums1:
#             for n2 in nums2:
#                 if n1 == n2:
#                     result.add(n1)
                    
#         return result
    
    
    # 문제풀이2: 이진검색으로 일치 여부 판별
#         result: Set = set()
#         nums2.sort()
#         for n1 in nums1:
#             # 이진검색으로 일치 여부 판별
#             i2 = bisect.bisect_left(nums2, n1)
#             if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
#                 result.add(n1)
                
#         return result
    
    
    # 문제풀이3: 투포인터로 일치 여부 판별
        result: Set = set()
        # 양쪽 모두 정렬
        nums1.sort()
        nums2.sort()
        i = j = 0
        # 투 포인터 우측으로 이동하며 일치 여부 판별
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
                
        return result