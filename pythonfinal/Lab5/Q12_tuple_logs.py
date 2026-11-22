from datetime import datetime
logs = []
while True:
    category = input("Log category (or done): ")
    if category.lower() == "done": break
    message = input("Message: ")
    logs.append((datetime.now(), category, message))
for log in logs:
    print(log)
print("Category-wise:")
for category in sorted(set(x[1] for x in logs)):
    print(category, [x[2] for x in logs if x[1] == category])
print("Hour-wise:")
for hour in sorted(set(x[0].hour for x in logs)):
    print(hour, [x[2] for x in logs if x[0].hour == hour])
