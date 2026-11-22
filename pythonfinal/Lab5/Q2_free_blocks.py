# 0 = full, 1 = empty
blocks = [0, 1, 1, 1, 0, 0, 1, 1]
needed = int(input("How many blocks do you need? "))
if blocks.count(1) >= needed:
    for i in range(len(blocks)):
        if needed and blocks[i] == 1:
            blocks[i] = 0
            needed -= 1
    print("Blocks allocated.")
else:
    print("Not enough free blocks.")
print("Blocks:", blocks)
