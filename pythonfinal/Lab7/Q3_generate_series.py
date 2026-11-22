# Generate an AP
start = int(input("Starting number: "))
difference = int(input("Common difference: "))
count = int(input("Number of terms: "))
series = [start + i * difference for i in range(count)]
print(series)
