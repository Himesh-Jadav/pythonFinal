# Q1-Q6: Map and Filter

# Password strength checker
def strength(password):
    score = sum([len(password) >= 8, any(c.isupper() for c in password),
                  any(c.islower() for c in password), any(c.isdigit() for c in password),
                  any(not c.isalnum() for c in password)])
    if score >= 4: return "S"
    elif score >= 3: return "M"
    return "W"

# Q1: list of strengths
passwords = input("Enter passwords separated by spaces: ").split()
print("Q1:", list(map(strength, passwords)))

# Q2: password -> strength dictionary
print("Q2:", dict(map(lambda p: (p, strength(p)), passwords)))

# Q3: filter only strong passwords
strong = list(filter(lambda p: strength(p) == "S", passwords))
print("Q3:", dict(map(lambda p: (p, strength(p)), strong)))

# Q4: map words to lengths
words = input("Enter words: ").split()
print("Q4:", list(map(lambda w: (w, len(w)), words)))

# Q5: Armstrong numbers from 1 to 10000
def armstrong(n):
    digits = str(n)
    return sum(int(d)**len(digits) for d in digits) == n
print("Q5:", list(filter(armstrong, range(1, 10001))))

# Q6: highest expenses day/week/month
from datetime import datetime
expenses = [('01-10-2026', 500), ('02-10-2026', 900), ('03-10-2026', 200),
            ('08-10-2026', 1200), ('15-10-2026', 700)]
daily = {}
weekly = {}
monthly = {}
for date, amount in expenses:
    d = datetime.strptime(date, "%d-%m-%Y")
    daily[date] = daily.get(date, 0) + amount
    week = (d.year, d.isocalendar().week)
    month = (d.year, d.month)
    weekly[week] = weekly.get(week, 0) + amount
    monthly[month] = monthly.get(month, 0) + amount
print("Q6 highest day:", max(daily, key=daily.get), max(daily.values()))
print("Q6 highest week:", max(weekly, key=weekly.get), max(weekly.values()))
print("Q6 highest month:", max(monthly, key=monthly.get), max(monthly.values()))
