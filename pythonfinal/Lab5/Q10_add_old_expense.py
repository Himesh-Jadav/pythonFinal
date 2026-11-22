expenses = ['01-10-2026',500, '01-10-2026',300, '02-10-2026',700, '02-10-2026',200, '03-10-2026',1000]
date = input("Enter expense date: ")
amount = float(input("Enter amount: "))
expenses.extend([date, amount])
daily = {}
for i in range(0, len(expenses), 2):
    d, amt = expenses[i], expenses[i+1]
    daily[d] = daily.get(d, 0) + amt
for d, total in sorted(daily.items()):
    print(d, ":", total)
print("Overall expense:", sum(daily.values()))
