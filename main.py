import twstock
from  twstock import BestFourPoint
import lxml
import pandas as pd
import matplotlib.pyplot as plt

stock_number = input('股票代碼：')
year = int(input('年份：'))
month = int(input('月份：'))
stock = twstock.Stock(stock_number)

print("股票代號:", stock.sid)
print("個日收盤價:", stock.price)
print("各日最高價：", stock.high)
print("個日最低價：", stock.low)
print("各日成交股數：", stock.capacity)
print("各日的日期：", stock.date)

ma_p = stock.moving_average(stock.price, 5)
print("五日均價：", ma_p)

ma_c = stock.moving_average(stock.capacity, 5)
print("五日均量：", ma_c)

ma_p_cont = stock.continuous(ma_p)
print("五日均價持續天數：", ma_p_cont)

ma_br = stock.ma_bias_ratio(5,10)
print("五日、十日乖離率：", ma_br)

ma_brp = stock.ma_bias_ratio_pivot(stock.price, 5, True)
print("正乖離率轉折位置：", ma_brp)
ma_brp2 = stock.ma_bias_ratio_pivot(stock.price, 5, False)
print("負乖離率轉折位置：", ma_brp2)

bfp = BestFourPoint(stock)
bfp_buy = bfp.best_four_point_to_buy()
print("是否為四大買點：", bfp_buy)
bfp_sell = bfp.best_four_point_to_sell()
print("是否為四大賣點：", bfp_sell)
bfp_result = bfp.best_four_point()
print("綜合判斷：", bfp_result)

data = stock.fetch(year, month)
df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")
plt.figure()
df[["close", "open", "high", "low"]].plot()
plt.show()
