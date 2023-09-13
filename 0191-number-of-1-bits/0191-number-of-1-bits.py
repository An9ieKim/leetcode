class Solution:
    def hammingWeight(self, n: int) -> int:
        # 문제풀이 1: 1의 개수 계산
#        return bin(n).count('1')
        
        # 문제풀이 2: 비트 연산
        count = 0
        while n:
            # 1을 뺀 값과 AND 연산 횟수 측정
            n &= n - 1
            count += 1
        return count