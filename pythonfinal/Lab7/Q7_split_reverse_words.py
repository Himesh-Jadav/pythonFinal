words = input("Enter sentence: ").split()
def transform(word):
    mid = len(word) // 2
    return word[:mid][::-1] + word[mid:][::-1]
result = {word: transform(word) for word in words}
print(result)
