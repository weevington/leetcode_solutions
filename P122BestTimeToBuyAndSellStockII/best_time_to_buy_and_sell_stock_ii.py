class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Given a list of numbers representing prices of a stock, returns the 
        maximum profit that can be obtained at the end of the interval. Each
        number represents prices spaced evenly (i.e. daily closing prices).

        You may complete as many transactions as you like (i.e., buy one and
        sell one share of the stock multiple times).

        Note: You may not engage in multiple transactions at the same time 
        (i.e., you must sell the stock before you buy again).

        Parameters
        ----------
        prices : List[int]
            Array representing prices
        
        Returns
        -------
        max_profit : int
            Maximum profit that can be achieved over the length of the
            interval.

        Input: [7,1,5,3,6,4]
        Output: 7
        Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), 
            profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 
            (price = 6), profit = 6-3 = 3.

        Input: [1,2,3,4,5]
        Output: 4
        Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5),
            profit = 5-1 = 4. Note that you cannot buy on day 1, buy on day 2 
            and sell them later, as you are engaging multiple transactions at
            the same time. You must sell before buying again.

        Input: [7,6,4,3,1]
        Output: 0
        Explanation: In this case, no transaction is done, i.e.
            max_profit = 0.
        """
        len_prices = len(prices)
        
        if len_prices < 2:
            return 0
        
        max_profit = 0
        
        for i in range(1, len_prices):
            if prices[i] - prices[i - 1] > 0:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit