class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    # 문제풀이: XOR 풀이
        result = 0
        for num in nums:
            result ^= num
        
        return result