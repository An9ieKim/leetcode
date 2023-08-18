class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
    
    # 문제풀이 1: 해시 테이블을 이용한 풀이
#         freqs = {}
#         count = 0
        
#         # 돌(stones)의 빈도 수 계산
#         for char in stones:
#             if char not in freqs:
#                 freqs[char] = 1
#             else:
#                 freqs[char] += 1
                
#         # 보석(jewels)의 빈도 수 합산
#         for char in jewels:
#             if char in freqs:
#                 count += freqs[char]
                
#         return count
        
    
    # 문제풀이 2: defaultdict을 이용한 비교 생략
#         freqs = collections.defaultdict(int)
#         count = 0
        
#         # 비교 없이 돌(stones)의 빈도 수 계산
#         for char in stones:
#             freqs[char] += 1
    
#         # 비교 없이 보석(jewels)의 빈도 수 합산
#         for char in jewels:
#             count += freqs[char]
        
#         return count
    
    
    # 문제풀이 3: counter로 계산 생략
#         freqs = collections.Counter(stones) # 돌(stones)의 빈도 수 계산
#         count = 0
        
#         # 비교 없이 보석(jewels)의 빈도 수 합산
#         for char in jewels:
#             count += freqs[char]
#         return count
    
    
    # 문제풀이 4: 파이썬다운 방식
        return sum(s in jewels for s in stones)