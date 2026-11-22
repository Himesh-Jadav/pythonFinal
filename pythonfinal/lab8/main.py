# Simple Python programs for Questions 1 to 9
# All programs use functions and run sequentially.

import math

# Q1: Factorial and nCr
def q1():
    print("\n--- Q1: Factorial and nCr ---")
    n = int(input("Enter n: "))
    r = int(input("Enter r: "))
    if n < 0 or r < 0 or r > n:
        print("Please enter valid values (n >= r >= 0).")
        return
    print("Factorial:", math.factorial(n))
    print("nCr:", math.comb(n, r))

# Q2: Matrix operations
def read_matrix(rows, cols, name):
    print(f"Enter {name} matrix row-wise:")
    return [[int(input(f"{name}[{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)]

def print_matrix(matrix):
    for row in matrix:
        print(row)

def q2():
    print("\n--- Q2: Matrix Operations ---")
    r = int(input("Rows: "))
    c = int(input("Columns: "))
    a = read_matrix(r, c, "A")
    b = read_matrix(r, c, "B")
    print("Addition:")
    print_matrix([[a[i][j] + b[i][j] for j in range(c)] for i in range(r)])
    print("Subtraction:")
    print_matrix([[a[i][j] - b[i][j] for j in range(c)] for i in range(r)])
    print("Multiplication (A x B):")
    if c == r:
        print_matrix([[sum(a[i][k] * b[k][j] for k in range(c)) for j in range(c)] for i in range(r)])
    else:
        print("Multiplication skipped: this simple program requires square matrices.")
    print("Transpose of A:")
    print_matrix([[a[i][j] for i in range(r)] for j in range(c)])

# Q3: Polynomial addition and subtraction
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
    print("\n--- Q3: Polynomial Addition and Subtraction ---")
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

# Q4: Password strength checker
def q4():
    print("\n--- Q4: Password Strength ---")
    password = input("Enter password: ")
    score = sum([len(password) >= 8, any(c.isupper() for c in password), any(c.islower() for c in password), any(c.isdigit() for c in password), any(not c.isalnum() for c in password)])
    if score <= 2:
        print("Weak password")
    elif score <= 4:
        print("Medium password")
    else:
        print("Strong password")

# Q5: Product dictionary with unique ID
def q5():
    print("\n--- Q5: Product Details ---")
    products = {}
    count = int(input("Number of products: "))
    for i in range(count):
        name = input("Product name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        product_id = f"P{i+1:03}"
        products[product_id] = {"name": name, "price": price, "quantity": quantity}
    print(products)

# Q6: Best cricket player and team
def q6():
    print("\n--- Q6: Best Player and Team ---")
    player = input("Enter your best cricket player: ")
    team = input("Enter your best cricket team: ")
    def best_player():
        return player
    def best_team():
        return team
    print("Best player:", best_player())
    print("Best team:", best_team())

# Q7: Synonyms for words in a sentence
def q7():
    print("\n--- Q7: Synonym Finder ---")
    synonyms = {"happy": ["joyful", "cheerful"], "sad": ["unhappy", "upset"], "big": ["large", "huge"], "small": ["tiny", "little"], "fast": ["quick", "rapid"]}
    sentence = input("Enter a sentence: ").lower()
    for word in sentence.split():
        word = word.strip(".,!?;:")
        if word in synonyms:
            print(word, "->", synonyms[word])

# Q8: Expense tracker
def q8():
    print("\n--- Q8: Expense Tracker ---")
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

# Q9: Phone book
def q9():
    print("\n--- Q9: Phone Book ---")
    contacts = {}
    while True:
        print("\n1. Add  2. Update  3. Remove  4. Search  5. Sort  6. Exit")
        choice = input("Choice: ")
        if choice == "1":
            name = input("Name: ")
            contacts[name] = {"phone": input("Phone: "), "email": input("Email: ")}
        elif choice == "2":
            name = input("Contact name to update: ")
            if name in contacts:
                contacts[name] = {"phone": input("New phone: "), "email": input("New email: ")}
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

# Run all question programs sequentially
def main():
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()
    q8()
    q9()
    print("\nAll programs completed.")

if __name__ == "__main__":
    main()
