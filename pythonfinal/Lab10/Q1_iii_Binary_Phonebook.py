import pickle

FILE = "phonebook.dat"
try:
    try:
        with open(FILE, "rb") as f: contacts = pickle.load(f)
    except FileNotFoundError:
        contacts = []
    while True:
        print("1 Add  2 View  3 Exit")
        choice = input("Choice: ")
        if choice == "1":
            contacts.append((input("Name: "), input("Phone: "), input("Email: ")))
            with open(FILE, "wb") as f: pickle.dump(contacts, f)
        elif choice == "2":
            for contact in contacts: print(contact)
        elif choice == "3": break
        else: print("Invalid choice")
except (OSError, pickle.PickleError) as e:
    print("File error:", e)
