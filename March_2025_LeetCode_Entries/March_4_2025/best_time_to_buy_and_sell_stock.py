class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # start with an initial value of positive infinity for min_price
        min_price = float('inf')
        # start with zero profit
        max_profit = 0
        
        for price in prices: 
            if price < min_price:
                # update minimum price, if lower is found
                min_price = price
            else:
                # update maximum profit
                max_profit = max(max_profit, price - min_price)
        return max_profit
        