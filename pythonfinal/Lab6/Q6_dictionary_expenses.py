expenses = {'01-10-2026': 800, '02-10-2026': 900, '01-10-2026': 300}
# Example data is dictionary-based; for repeated dates, use list of pairs:
items = [('01-10-2026',500), ('01-10-2026',300), ('02-10-2026',700)]
totals = {}
for date, amount in items:
    totals[date] = totals.get(date, 0) + amount
print(totals)
