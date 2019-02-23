# 5.6
#
# Write a program that takes an array denoting the daily stock price, and retums the maximum profit
# that could be made by buying and then selling one share of that stock. There is no need to buy if
# no profit is possible.


def max_possible_profit(prices):
    max_profit_last, min_price_so_far = 0,  prices[0]
    max_profit = 0
    for price in prices:
        max_profit_last = price - min_price_so_far
        min_price_so_far = min(price,min_price_so_far)
        max_profit = max(max_profit,max_profit_last)
    return max_profit

ticker = [310, 315, 275, 260, 270, 290, 230, 255, 250]

print(max_possible_profit(ticker))
