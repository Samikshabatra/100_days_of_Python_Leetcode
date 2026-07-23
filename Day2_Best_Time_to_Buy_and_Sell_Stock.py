"""
Day 2 - Best Time to Buy and Sell Stock  (LeetCode #121, Easy)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

The task: I'm given an array `prices` where prices[i] is the price of a stock on
day i. I have to buy on one day and sell on a *later* day, and return the maximum
profit I can make. If there's no way to make a profit, I return 0.

I solved this two ways.

Approach 1 - Brute force (my first attempt):
    I tried every possible buy day i paired with every later sell day j, worked out
    profit = prices[j] - prices[i], and kept the biggest profit I found. It's the
    most direct reading of the problem, but the nested loop makes it O(n^2) time,
    which is far too slow once the array gets large. Space is O(1).

Approach 2 - One pass (my optimized solution):
    I noticed I don't actually need to re-check every pair. Going left to right, the
    best profit from selling *today* is simply today's price minus the cheapest price
    I've seen so far. So I keep track of `min_price` as I walk the array, and update
    `max_profit` whenever selling today beats my current best. Since the minimum is
    always from a day before the one I'm on, the "buy before you sell" rule takes
    care of itself. That's a single scan: O(n) time and O(1) space.

Approach 2 is the one I'd submit - it turns the nested loop into one clean pass.
"""


class Solution(object):
    # Approach 1 - Brute force  |  Time: O(n^2)  |  Space: O(1)
    def max_profit_bruteforce(self, prices):
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit

    # Approach 2 - One pass (optimized)  |  Time: O(n)  |  Space: O(1)
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # -> 5  (buy at 1, sell at 6)
    print(sol.maxProfit([7, 6, 4, 3, 1]))     # -> 0  (prices only fall, so no trade)
