import talib
import yfinance as yf

data = yf.download("META", start="2022-10-01", end="2022-11-01", interval="5m")

# print(data)

num = talib.CDLHAMMER(data["Open"], data["High"], data["Low"], data["Close"])
# print(num)
print(num[num != 0])
