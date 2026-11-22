import csv

FILE = "phonebook.csv"
try:
    try:
        with open(FILE, newline="") as f: contacts = list(csv.reader(f))
    except FileNotFoundError:
        contacts = []
    while True:
        print("1 Add  2 View  3 Exit")
        choice = input("Choice: ")
        if choice == "1":
            contacts.append([input("Name: "), input("Phone: "), input("Email: ")])
            with open(FILE, "w", newline="") as f: csv.writer(f).writerows(contacts)
        elif choice == "2":
            for row in contacts: print(row)
        elif choice == "3": break
        else: print("Invalid choice")
except OSError as e:
    print("File error:", e)
