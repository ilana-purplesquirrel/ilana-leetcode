# in-class solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            # there aren't no two days for buying and selling
            return 0

        # n^2 solution:

        # setup
        profit = 0

        # last element in profits
        # outer loop: i, 0 -> end of prices
        for i in range(0, len(prices) - 1):
            cur_profit = 0
        #   inner loop: j, from i+1 -> end of prices
            for j in range(i+1, len(prices)):
                cur_profit = max(cur_profit, prices[j]-prices[i])
            profit = max(cur_profit, profit)

        return profit

        # time complexity(n^2)
