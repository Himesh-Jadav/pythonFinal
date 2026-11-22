# Enter each payment as a tuple (name, amount)
payments = [('A', 1200), ('B', 800), ('C', 500)]
people = dict(payments)
total = sum(people.values())
share = total / len(people)
print("Share per person:", share)
for name, paid in people.items():
    print(name, "paid", paid, "balance", round(paid-share, 2))
# Positive balance is owed to that person; negative means they owe.
creditors = [[n, round(v-share, 2)] for n, v in people.items() if v-share > 0]
debtors = [[n, round(share-v, 2)] for n, v in people.items() if v-share < 0]
for debtor, amount in debtors:
    for creditor, credit in creditors:
        settle = min(amount, credit)
        if settle:
            print(debtor, "owes", creditor, settle)
            amount -= settle
            credit -= settle
