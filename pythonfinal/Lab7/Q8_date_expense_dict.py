items = [('01-10-2026', 500), ('01-10-2026', 300), ('02-10-2026', 700)]
expenses = {date: sum(amount for d, amount in items if d == date) for date in set(d for d, amount in items)}
print(expenses)
