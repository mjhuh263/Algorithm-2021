# LeetCode # 121 : Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        while prices:
            leng = len(prices)
            profit = 0
            min_price = prices[0]
            
            for i in range(1,leng):
                profit = max(profit, prices[i] - min_price)
                min_price = min(min_price, prices[i])
                
            return profit