answer_key = ('A', 'B', 'C', 'D')
students = {'Ravi': ('A','B','C','A'), 'Asha': ('A','D','C','D')}
scores = {}
for name, answers in students.items():
    scores[name] = sum(4 if a == key else -1 for a, key in zip(answers, answer_key))
print(scores)
