import math

def q1():
    print("\n--- Factorial and nCr ---")
    n = int(input("Enter n: "))
    r = int(input("Enter r: "))
    if n < 0 or r < 0 or r > n:
        print("Invalid values.")
        return
    print("Factorial:", math.factorial(n))
    print("nCr:", math.comb(n, r))


def read_matrix(rows, cols, name):
    print(f"Enter {name} matrix:")
    return [[int(input(f"{name}[{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)]


def print_matrix(matrix):
    for row in matrix:
        print(row)


def q2():
    print("\n--- Matrix Operations ---")
    r = int(input("Rows: "))
    c = int(input("Columns: "))

    a = read_matrix(r, c, "A")
    b = read_matrix(r, c, "B")

    print("Addition:")
    print_matrix([[a[i][j] + b[i][j] for j in range(c)] for i in range(r)])

    print("Subtraction:")
    print_matrix([[a[i][j] - b[i][j] for j in range(c)] for i in range(r)])

    print("Multiplication (A x B):")
    if r == c:
        print_matrix([[sum(a[i][k] * b[k][j] for k in range(c)) for j in range(c)] for i in range(r)])
    else:
        print("Multiplication requires square matrices.")

    print("Transpose of A:")
    print_matrix([[a[i][j] for i in range(r)] for j in range(c)])


def read_poly():
    poly = {}
    terms = int(input("Number of terms: "))
    for _ in range(terms):
        coef = int(input("Coefficient: "))
        power = int(input("Power: "))
        poly[power] = poly.get(power, 0) + coef
    return poly


def show_poly(poly):
    terms = []
    for p in sorted(poly, reverse=True):
        c = poly[p]
        if c:
            terms.append(f"{c}x^{p}" if p else str(c))
    print(" + ".join(terms) if terms else "0")


def q3():
    print("\n--- Polynomial Addition and Subtraction ---")
    print("Polynomial 1:")
    a = read_poly()
    print("Polynomial 2:")
    b = read_poly()

    add = dict(a)
    sub = dict(a)

    for p, c in b.items():
        add[p] = add.get(p, 0) + c
        sub[p] = sub.get(p, 0) - c

    print("Addition:")
    show_poly(add)

    print("Subtraction:")
    show_poly(sub)


def q4():
    print("\n--- Password Strength ---")
    password = input("Enter password: ")

    score = sum([
        len(password) >= 8,
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        any(not c.isalnum() for c in password)
    ])

    if score <= 2:
        print("Weak password")
    elif score <= 4:
        print("Medium password")
    else:
        print("Strong password")


def q5():
    print("\n--- Product Details ---")
    products = {}
    count = int(input("Number of products: "))

    for i in range(count):
        name = input("Product name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        product_id = f"P{i+1:03}"

        products[product_id] = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

    print("Product Details:")
    print(products)


def q6():
    def best_player():
        players = {
            "Virat Kohli": 100,
            "Rohit Sharma": 85,
            "MS Dhoni": 75
        }

        best = max(players, key=players.get)
        print("Best Player:", best)
        print("Runs:", players[best])


    def best_team():
        teams = {
            "India": 250,
            "Australia": 220,
            "England": 180
        }

        best = max(teams, key=teams.get)
        print("Best Team:", best)
        print("Runs:", teams[best])


    best_player()
    best_team()


def q7():
    print("\n--- Synonym Finder ---")

    synonyms = {
        "happy": ["joyful", "cheerful"],
        "sad": ["unhappy", "upset"],
        "big": ["large", "huge"],
        "small": ["tiny", "little"],
        "fast": ["quick", "rapid"]
    }

    sentence = input("Enter a sentence: ").lower()

    for word in sentence.split():
        word = word.strip(".,!?;:")
        if word in synonyms:
            print(word, "->", synonyms[word])


def q8():
    print("\n--- Expense Tracker ---")
    expenses = []

    while True:
        name = input("Expense name (or 'done'): ")

        if name.lower() == "done":
            break

        amount = float(input("Amount: "))
        expenses.append((name, amount))

    for name, amount in expenses:
        print(name, "-", amount)

    print("Total expense:", sum(amount for _, amount in expenses))


def q9():
    print("\n--- Phone Book ---")
    contacts = {}

    while True:
        print("\n1. Add  2. Update  3. Remove  4. Search  5. Sort  6. Exit")
        choice = input("Choice: ")

        if choice == "1":
            name = input("Name: ")
            contacts[name] = {
                "phone": input("Phone: "),
                "email": input("Email: ")
            }

        elif choice == "2":
            name = input("Contact name to update: ")
            if name in contacts:
                contacts[name] = {
                    "phone": input("New phone: "),
                    "email": input("New email: ")
                }
            else:
                print("Contact not found.")

        elif choice == "3":
            name = input("Contact name to remove: ")
            print("Removed." if contacts.pop(name, None) is not None else "Contact not found.")

        elif choice == "4":
            name = input("Contact name to search: ")
            print(contacts.get(name, "Contact not found."))

        elif choice == "5":
            for name in sorted(contacts):
                print(name, contacts[name])

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Factorial and nCr")
        print("2. Matrix Operations")
        print("3. Polynomial Addition and Subtraction")
        print("4. Password Strength Checker")
        print("5. Product Details")
        print("6. Best Cricket Player and Team")
        print("7. Synonym Finder")
        print("8. Expense Tracker")
        print("9. Phone Book")
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
        elif choice == "0":
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
