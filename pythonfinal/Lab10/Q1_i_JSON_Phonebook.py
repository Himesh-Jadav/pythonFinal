import json

FILE = "phonebook.json"
try:
    try:
        with open(FILE) as f: contacts = json.load(f)
    except FileNotFoundError:
        contacts = {}
    while True:
        print("1 Add  2 View  3 Exit")
        choice = input("Choice: ")
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            contacts[name] = {"phone": phone, "email": email}
            with open(FILE, "w") as f: json.dump(contacts, f, indent=2)
        elif choice == "2":
            print(contacts)
        elif choice == "3": break
        else: print("Invalid choice")
except (ValueError, OSError) as e:
    print("File error:", e)
