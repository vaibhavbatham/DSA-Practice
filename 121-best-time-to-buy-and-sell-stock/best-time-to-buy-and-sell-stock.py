class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_Price = float('inf')
        max_Profit = 0
        for i in range(len(prices)):
            min_Price = min (min_Price , prices[i])
            max_Profit = max(max_Profit , prices[i] - min_Price)

        return max_Profit