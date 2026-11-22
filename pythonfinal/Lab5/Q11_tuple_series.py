# Arithmetic progression (AP) or geometric progression (GP)
series = tuple(map(int, input("Enter series values: ").split()))
kind = input("AP or GP? ").upper()
count = int(input("How many terms to extend? "))
extended = list(series)
if kind == "AP":
    diff = series[-1] - series[-2]
    for _ in range(count):
        extended.append(extended[-1] + diff)
elif kind == "GP":
    ratio = series[-1] / series[-2]
    for _ in range(count):
        extended.append(extended[-1] * ratio)
print(tuple(extended))
