# in-class solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            # there aren't no two days for buying and selling
            return 0

        # setup: two pointers
        l = 0
        r = l+1
        profit = 0

        while l<(len(prices) - 1) and r<len(prices):
            # if the current r value is > the current l val:
            if prices[r] > prices[l]:
               profit = max(profit, prices[r]-prices[l])
               r += 1
            else:
                # right val is less than left val
                # so, move left to the right position
                l = r
                r += 1

        return profit

        # time complexity: O(1)
