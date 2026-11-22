text = input("Enter a string: ")
counts = {ch: text.count(ch) for ch in text}
print(counts)
