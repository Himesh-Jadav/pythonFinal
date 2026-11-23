
import re
from datetime import datetime


def strength(password):
    score = sum([
        len(password) >= 8,
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        any(not c.isalnum() for c in password)
    ])
    if score >= 4:
        return "S"
    elif score >= 3:
        return "M"
    return "W"


def q1():
    passwords = input("Enter passwords separated by spaces: ").split()
    print("Q1:", list(map(strength, passwords)))


def q2():
    passwords = input("Enter passwords separated by spaces: ").split()
    print("Q2:", dict(map(lambda p: (p, strength(p)), passwords)))


def q3():
    passwords = input("Enter passwords separated by spaces: ").split()
    strong = list(filter(lambda p: strength(p) == "S", passwords))
    print("Q3:", dict(map(lambda p: (p, strength(p)), strong)))


def q4():
    words = input("Enter words: ").split()
    print("Q4:", list(map(lambda w: (w, len(w)), words)))


def q5():
    def armstrong(n):
        digits = str(n)
        return sum(int(d) ** len(digits) for d in digits) == n

    print("Q5:", list(filter(armstrong, range(1, 10001))))


def q6():
    expenses = [
        ('01-10-2026', 500),
        ('02-10-2026', 900),
        ('03-10-2026', 200),
        ('08-10-2026', 1200),
        ('15-10-2026', 700)
    ]

    daily = {}
    weekly = {}
    monthly = {}

    for date, amount in expenses:
        d = datetime.strptime(date, "%d-%m-%Y")

        daily[date] = daily.get(date, 0) + amount

        week = (d.year, d.isocalendar().week)
        month = (d.year, d.month)

        weekly[week] = weekly.get(week, 0) + amount
        monthly[month] = monthly.get(month, 0) + amount

    print("Highest day:", max(daily, key=daily.get), max(daily.values()))
    print("Highest week:", max(weekly, key=weekly.get), max(weekly.values()))
    print("Highest month:", max(monthly, key=monthly.get), max(monthly.values()))


def q7():
    def hanoi(n, source, target, spare):
        if n == 1:
            print("Move disk 1 from", source, "to", target)
        else:
            hanoi(n-1, source, spare, target)
            print("Move disk", n, "from", source, "to", target)
            hanoi(n-1, spare, target, source)

    n = int(input("Number of disks: "))
    if n <= 0:
        print("Enter a positive number.")
    else:
        hanoi(n, "A", "C", "B")


def q8():
    def binary_search(a, key, low, high):
        if low > high:
            return -1

        mid = (low + high) // 2

        if a[mid] == key:
            return mid
        if key < a[mid]:
            return binary_search(a, key, low, mid-1)

        return binary_search(a, key, mid+1, high)

    nums = list(map(int, input("Enter sorted numbers: ").split()))
    key = int(input("Search value: "))

    if nums != sorted(nums):
        print("Please enter numbers in sorted order.")
    else:
        print("Index:", binary_search(nums, key, 0, len(nums)-1))


def q9():
    sentence = input("Enter sentence: ")

    corrupt = lambda w: (w[1:] + w[0] + "ho") if len(w) > 1 else w + "ho"

    print("Q9:", " ".join(map(corrupt, sentence.split())))


def q10():
    sentences = input("Enter sentences separated by |: ").split("|")

    def reverse_halves(word):
        mid = len(word) // 2
        return word[:mid][::-1] + word[mid:][::-1]

    print("Q10:", list(map(
        lambda s: " ".join(map(reverse_halves, s.split())),
        sentences
    )))


def q11():
    hashtags = input("Enter hashtags separated by spaces: ").split()

    print("Q11:", list(map(
        lambda h: re.sub(
            r'([a-z])([A-Z])',
            r'\1 \2',
            h.lstrip("#")
        ).replace("_", " "),
        hashtags
    )))


def q12():
    prices = list(map(float, input("Enter prices: ").split()))
    print("Q12:", list(map(lambda p: round(p * 1.18, 2), prices)))


def q13():
    temps = list(map(float, input("Enter temperatures: ").split()))

    print("Hot:", list(filter(lambda t: t >= 30, temps)))
    print("Cold:", list(filter(lambda t: t <= 15, temps)))


def q14():
    data = [('Mon', 32), ('Tue', 12), ('Wed', 29), ('Thu', 8)]

    print("Hot days:", list(filter(lambda x: x[1] >= 30, data)))
    print("Cold days:", list(filter(lambda x: x[1] <= 15, data)))


def q15():
    items = [('Pen', 50), ('Book', 200), ('Bag', 800)]

    print("Q15:", list(map(
        lambda x: (x[0], round(x[1] * 0.90, 2)),
        items
    )))


def q16():
    marks = {
        101: [80, 90, 70],
        102: [60, 75, 85]
    }

    print("Q16:", dict(map(
        lambda x: (x[0], round(sum(x[1]) / len(x[1]), 2)),
        marks.items()
    )))


def q17():
    shares = {
        'Mon': 100,
        'Tue': 120,
        'Wed': 115,
        'Thu': 140,
        'Fri': 130
    }

    print("Q17 highest:", max(shares, key=shares.get), max(shares.values()))


def q18():
    nums = list(map(int, input("Enter numbers: ").split()))

    print("Q18:", list(map(
        lambda x: x * x,
        filter(lambda x: x % 2 == 0, nums)
    )))


def q19():
    print("String:", "".join(map(lambda c: c.upper(), "python")))

    print("List:", list(filter(
        lambda x: x > 0,
        [-3, 2, 0, 5]
    )))

    print("Tuple:", tuple(map(lambda x: x * x, (1, 2, 3))))

    marks_dict = {'A': 45, 'B': 80, 'C': 60}

    print("Dictionary:", dict(filter(
        lambda x: x[1] >= 50,
        marks_dict.items()
    )))


def main():
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Password Strength List")
        print("2. Password Strength Dictionary")
        print("3. Filter Strong Passwords")
        print("4. Words and Lengths")
        print("5. Armstrong Numbers")
        print("6. Highest Expenses")
        print("7. Tower of Hanoi")
        print("8. Recursive Binary Search")
        print("9. Piglet Word Corruption")
        print("10. Reverse Halves of Words")
        print("11. Hashtag to Words")
        print("12. Add GST to Prices")
        print("13. Hot and Cold Temperatures")
        print("14. Hot and Cold Days")
        print("15. Apply Discount")
        print("16. Student Percentages")
        print("17. Highest Share Price")
        print("18. Even Numbers and Squares")
        print("19. Map and Filter Examples")
        print("0. Exit")
        print("===============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            q1()
        elif choice == "2":
            q2()
        elif choice == "3":
            q3()
        elif choice == "4":
            q4()
        elif choice == "5":
            q5()
        elif choice == "6":
            q6()
        elif choice == "7":
            q7()
        elif choice == "8":
            q8()
        elif choice == "9":
            q9()
        elif choice == "10":
            q10()
        elif choice == "11":
            q11()
        elif choice == "12":
            q12()
        elif choice == "13":
            q13()
        elif choice == "14":
            q14()
        elif choice == "15":
            q15()
        elif choice == "16":
            q16()
        elif choice == "17":
            q17()
        elif choice == "18":
            q18()
        elif choice == "19":
            q19()
        elif choice == "0":
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
