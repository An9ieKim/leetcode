class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
    ### 문제풀이 1: 브루트 포스로 계산 (타임아웃)
#         max_price = 0
        
#         for i, price in enumerate(prices):
#             for j in range(i, len(prices)):
#                 max_price = max(prices[j] - price, max_price)
    
#         return max_price
    
    ### 문제풀이 2: 저점과 현재 값과의 차이 계산
        profit = 0
        min_price = sys.maxsize
        
        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            
        return profit