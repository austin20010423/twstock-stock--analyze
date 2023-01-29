import twstock
import lxml
import pandas as pd

stock_number = input()

stock = twstock.Stock(stock_number)
print("股票代號:", stock.sid)
print("個日收盤價:", stock.price)
print("各日最高價：", stock.high)
print("個日最低價：", stock.low)
print("各日成交股數：", stock.capacity)
print("各日的日期：", stock.date)

data = stock.fetch(2021, 11)
df =