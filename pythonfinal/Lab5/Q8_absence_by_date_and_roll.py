data = ['25-9-2026',51,101,67, '26-9-2026',51,101,68,59, '27-9-2026',101,51,28,65]
by_date = {}
counts = {}
date = None
for item in data:
    if isinstance(item, str):
        date = item
        by_date[date] = []
    else:
        by_date[date].append(item)
        counts[item] = counts.get(item, 0) + 1
for date, rolls in by_date.items():
    print("Absent students on", date + ":", *rolls)
for roll, count in sorted(counts.items()):
    print(f"Total classes absent by roll no {roll}: {count}")
