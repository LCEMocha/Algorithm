class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = sys.maxsize
        high = 0
        price = 0
        
        if prices == sorted(prices, reverse = True):
            return 0
        
        for i in range(len(prices)-1):
            if prices[i] < low and prices[i] < prices[i+1]:
                low = prices[i]
                high = max(x for x in prices[i:] if x > low)
                price = max(price, high-low)
        return price