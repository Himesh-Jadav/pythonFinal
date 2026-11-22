code = input("Enter train code (name|time|source|destination): ")
train = tuple(code.split("|"))
if len(train) == 4:
    print("Name:", train[0], "Time:", train[1], "Source:", train[2], "Destination:", train[3])
else:
    print("Invalid code")
