class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - buy)
        return maxProfit
        