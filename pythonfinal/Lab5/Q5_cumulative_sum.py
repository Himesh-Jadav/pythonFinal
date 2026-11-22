nums = list(map(int, input("Enter numbers: ").split()))
total = 0
result = []
for n in nums:
    total += n
    result.append(total)
print(result)
