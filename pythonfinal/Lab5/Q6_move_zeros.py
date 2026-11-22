nums = list(map(int, input("Enter numbers: ").split()))
result = [n for n in nums if n != 0] + [0] * nums.count(0)
print(result)
