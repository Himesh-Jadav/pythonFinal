nums = list(map(int, input("Enter numbers: ").split()))
cubes = [n**3 for n in nums if n % 2 == 0]
print(cubes)
