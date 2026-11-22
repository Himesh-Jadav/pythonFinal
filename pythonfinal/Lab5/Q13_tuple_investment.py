# Each tuple: (date, stock, buy_price, sell_price)
investments = [('25-9-2026', 'Birla Cements', 500, 400)]
stock_pl, date_pl = {}, {}
for date, stock, buy, sell in investments:
    pl = sell - buy
    stock_pl[stock] = stock_pl.get(stock, 0) + pl
    date_pl[date] = date_pl.get(date, 0) + pl
print("Stock-wise P/L:", stock_pl)
print("Date-wise P/L:", date_pl)
print("Overall P/L:", sum(stock_pl.values()))
