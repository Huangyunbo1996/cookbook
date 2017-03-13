#-*- coding:utf-8 -*-

if __name__ == '__main__':

    prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
    }

    max_price = max(zip(prices.values(),prices.keys()))
    min_price = min(zip(prices.values(),prices.keys()))
    sorted_price = sorted(zip(prices.values(),prices.keys()))

    print('max:',max_price)
    print('min:',min_price)
    print('sorted:',sorted_price)