expenses = ['01-10-2026',500, '01-10-2026',300, '02-10-2026',700, '02-10-2026',200, '03-10-2026',1000]
daily = {}
for i in range(0, len(expenses), 2):
    date, amount = expenses[i], expenses[i+1]
    daily[date] = daily.get(date, 0) + amount
for date, total in daily.items():
    print(date, ":", total)
print("Overall expense:", sum(daily.values()))
