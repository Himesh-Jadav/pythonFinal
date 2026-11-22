items = [('01-10-2026','Food',500), ('01-10-2026','Travel',300), ('02-10-2026','Food',700)]
totals = {}
for date, category, amount in items:
    totals.setdefault(date, {}).setdefault(category, 0)
    totals[date][category] += amount
print(totals)
