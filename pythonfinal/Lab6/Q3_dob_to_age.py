from datetime import date
people = {'Asha': '2000-05-10', 'Ravi': '1998-12-01'}
ages = {}
today = date.today()
for name, dob in people.items():
    y, m, d = map(int, dob.split('-'))
    ages[name] = today.year-y-((today.month, today.day) < (m, d))
print(ages)
