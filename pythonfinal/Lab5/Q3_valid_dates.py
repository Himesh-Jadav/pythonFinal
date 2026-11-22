import re
dates = input("Enter dates separated by spaces (DD-MM-YYYY): ").split()
pattern = r'^(0?[1-9]|[12][0-9]|3[01])-(0?[1-9]|1[0-2])-\d{4}$'
for date in dates:
    if re.match(pattern, date):
        print("Valid format:", date)
