prices = [7, 1, 5, 3, 6, 4]

profit = 0
min = prices[0]
for i in prices:
    if i < min:
        min = i

    curr_profit = i - min
    if curr_profit > profit:
        profit = curr_profit

print(profit)