class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        
        maxProfit = 0
        smallestBuy = float('inf')
        for price in prices:
            if price < smallestBuy:
                smallestBuy = price
            else:
                maxProfit = max(maxProfit, price - smallestBuy)
            
        return maxProfit            
        