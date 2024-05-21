"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""


def max_profit(prices):
    if len(prices) == 1:
        return 0

    buy = prices[0]
    ans = 0
    for day in prices[1:]:
        profit = day - buy
        if profit > 0:
            if profit > ans:
                ans = profit
        else:
            buy = day
    return ans


prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))

prices = [7, 6, 4, 3, 1]
print(max_profit(prices))

prices = [10, 15, 7, 10, 1, 15, 1]
print(max_profit(prices))
