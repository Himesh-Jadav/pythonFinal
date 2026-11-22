# Q9-Q19: Map, Filter and Lambda

# Q9: Piglet-style corruption of every word
sentence = input("Q9 sentence: ")
corrupt = lambda w: (w[1:] + w[0] + "ho") if len(w) > 1 else w + "ho"
print("Q9:", " ".join(map(corrupt, sentence.split())))

# Q10: reverse each half of each word in multiple sentences
sentences = input("Q10 enter sentences separated by |: ").split("|")
def reverse_halves(word):
    mid = len(word) // 2
    return word[:mid][::-1] + word[mid:][::-1]
print("Q10:", list(map(lambda s: " ".join(map(reverse_halves, s.split())), sentences)))

# Q11: turn hashtags into words (CamelCase and underscores)
hashtags = input("Q11 hashtags separated by spaces: ").split()
import re
print("Q11:", list(map(lambda h: re.sub(r'([a-z])([A-Z])', r'\\1 \\2', h.lstrip("#")).replace("_", " "), hashtags)))

# Q12: add GST to item prices (18%)
prices = list(map(float, input("Q12 prices: ").split()))
print("Q12:", list(map(lambda p: round(p * 1.18, 2), prices)))

# Q13: hot and cold temperatures (thresholds: >=30 hot, <=15 cold)
temps = list(map(float, input("Q13 temperatures: ").split()))
print("Hot:", list(filter(lambda t: t >= 30, temps)))
print("Cold:", list(filter(lambda t: t <= 15, temps)))

# Q14: (day, temperature) tuples
data = [('Mon', 32), ('Tue', 12), ('Wed', 29), ('Thu', 8)]
print("Q14 hot days:", list(filter(lambda x: x[1] >= 30, data)))
print("Q14 cold days:", list(filter(lambda x: x[1] <= 15, data)))

# Q15: apply offer to (item, price) tuples; 10% discount
items = [('Pen', 50), ('Book', 200), ('Bag', 800)]
print("Q15:", list(map(lambda x: (x[0], round(x[1]*0.90, 2)), items)))

# Q16: roll number -> marks list; output percentages
marks = {101: [80, 90, 70], 102: [60, 75, 85]}
print("Q16:", dict(map(lambda x: (x[0], round(sum(x[1])/len(x[1]), 2)), marks.items())))

# Q17: share prices during a week
shares = {'Mon': 100, 'Tue': 120, 'Wed': 115, 'Thu': 140, 'Fri': 130}
print("Q17 highest:", max(shares, key=shares.get), max(shares.values()))

# Q18: sample practice - filter even numbers, then square using map
nums = list(map(int, input("Q18 numbers: ").split()))
print("Q18:", list(map(lambda x: x*x, filter(lambda x: x % 2 == 0, nums))))

# Q19: one simple example each: string, list, tuple, dictionary
# String: map uppercase letters
print("String:", "".join(map(lambda c: c.upper(), "python")))
# List: filter positives
print("List:", list(filter(lambda x: x > 0, [-3, 2, 0, 5])))
# Tuple: map tuple elements to squares
print("Tuple:", tuple(map(lambda x: x*x, (1, 2, 3))))
# Dictionary: filter entries with value >= 50
marks_dict = {'A': 45, 'B': 80, 'C': 60}
print("Dictionary:", dict(filter(lambda x: x[1] >= 50, marks_dict.items())))
