# -*- coding: utf-8 -*-
"""Assignment 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q26z1h0gskuyEYORq0LLk3VDp9rhEU9P
"""

def best_buy_sell_prices(prices):
    if not prices or len(prices) < 2:
        return None, None

    min_price = prices[0]
    best_buy = prices[0]
    best_sell = prices[1]
    max_profit = best_sell - best_buy

    for price in prices[1:]:

        if price - min_price > max_profit:
            max_profit = price - min_price
            best_buy = min_price
            best_sell = price


        if price < min_price:
            min_price = price

    return best_buy, best_sell


prices = [5, 2, 1, 6, 9, 7]
buy, sell = best_buy_sell_prices(prices)

print("Best Buy Price:", buy)
print("Best Sell Price:", sell)