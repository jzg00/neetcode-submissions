class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # algorithm:
        # if len(prices) < 2: return 0
        # we use two pointers: buy and sell, starting at the beginning of the input array
        # we keep track of the current profit and update it using max(profit, sell - buy)
        # if the sell pointer value is less than the buy pointer value, move buy to the sell position (that is our new lowest buy)
        # if sell is higher value than the buy, we only move the sell pointer

        if len(prices) < 2:
            return 0
        
        buy, sell = 0, 1
        profit = 0
        
        for i in range(len(prices) - 1):
            profit = max(prices[sell] - prices[buy], profit)

            if prices[sell] < prices[buy]:
                buy = sell
                sell += 1
            else:
                sell += 1

        return profit