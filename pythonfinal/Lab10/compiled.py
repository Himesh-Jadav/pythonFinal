import os
import json
import csv
import pickle

JSON_FILE = "phonebook.json"
CSV_FILE = "phonebook.csv"
BINARY_FILE = "phonebook.dat"


# =====================================================
# time conversion: checks and class
# (in the folder version these are checks.py and converter.py
#  inside the timeconv package)
# =====================================================
def check_time(hour, minute, second):
    # checks 24 hour values
    if hour < 0 or hour > 23:
        raise ValueError("Hour must be between 0 and 23")
    if minute < 0 or minute > 59:
        raise ValueError("Minute must be between 0 and 59")
    if second < 0 or second > 59:
        raise ValueError("Second must be between 0 and 59")


def check_12_hour(hour):
    # checks hour of 12 hour format
    if hour < 1 or hour > 12:
        raise ValueError("Hour must be between 1 and 12 in 12 hour format")


class TimeConverter:
    def __init__(self):
        # time is always stored in 24 hour format
        self.hour = 0
        self.minute = 0
        self.second = 0

    # ----- setting the time -----
    def set_24_hour(self, text):
        # text looks like 18:45:30
        parts = text.strip().split(":")
        if len(parts) != 3:
            raise ValueError("Time must be in hh:mm:ss format")
        hour = int(parts[0])
        minute = int(parts[1])
        second = int(parts[2])
        check_time(hour, minute, second)
        self.hour = hour
        self.minute = minute
        self.second = second

    def set_12_hour(self, text):
        # text looks like 06:45:30 PM
        words = text.strip().split()
        if len(words) != 2:
            raise ValueError("Time must be in hh:mm:ss AM/PM format")
        period = words[1].upper()
        if period != "AM" and period != "PM":
            raise ValueError("Write AM or PM at the end")

        parts = words[0].split(":")
        if len(parts) != 3:
            raise ValueError("Time must be in hh:mm:ss AM/PM format")
        hour = int(parts[0])
        minute = int(parts[1])
        second = int(parts[2])
        check_12_hour(hour)

        # convert to 24 hour
        if period == "AM" and hour == 12:
            hour = 0
        elif period == "PM" and hour != 12:
            hour = hour + 12
        check_time(hour, minute, second)
        self.hour = hour
        self.minute = minute
        self.second = second

    def set_seconds(self, total):
        if total < 0 or total > 86399:
            raise ValueError("Seconds must be between 0 and 86399")
        self.hour = total // 3600
        self.minute = (total % 3600) // 60
        self.second = total % 60

    # ----- getting the time in different formats -----
    def get_24_hour(self):
        return "%02d:%02d:%02d" % (self.hour, self.minute, self.second)

    def get_12_hour(self):
        if self.hour < 12:
            period = "AM"
        else:
            period = "PM"
        hour = self.hour % 12
        if hour == 0:
            hour = 12
        return "%02d:%02d:%02d %s" % (hour, self.minute, self.second, period)

    def get_seconds(self):
        return self.hour * 3600 + self.minute * 60 + self.second


# =====================================================
# common phonebook operations (no exception handling)
# =====================================================
def print_phonebook_menu():
    print("\n--- PHONEBOOK ---")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("0. Back")


def find_contact(contacts, name):
    for c in contacts:
        if c["name"].lower() == name.lower():
            return c
    return None


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts.append({"name": name, "phone": phone})
    print("Contact added")


def view_contacts(contacts):
    if len(contacts) == 0:
        print("Phonebook is empty")
    for c in contacts:
        print(c["name"], "-", c["phone"])


def search_contact(contacts):
    key = input("Enter name to search: ").lower()
    found = list(filter(lambda c: key in c["name"].lower(), contacts))
    if len(found) == 0:
        print("Contact not found")
    for c in found:
        print(c["name"], "-", c["phone"])


def update_contact(contacts):
    name = input("Enter name to update: ")
    contact = find_contact(contacts, name)
    contact["phone"] = input("Enter new phone number: ")
    print("Contact updated")


def delete_contact(contacts):
    name = input("Enter name to delete: ")
    contact = find_contact(contacts, name)
    contacts.remove(contact)
    print("Contact deleted")


# =====================================================
# 1. phonebook using json file (no exception handling)
# =====================================================
def phonebook_json():
    contacts = []
    if os.path.exists(JSON_FILE):
        f = open(JSON_FILE, "r")
        contacts = json.load(f)
        f.close()

    while True:
        print_phonebook_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "0":
            break
        else:
            print("Wrong choice, try again")

        if choice in ["1", "4", "5"]:
            f = open(JSON_FILE, "w")
            json.dump(contacts, f, indent=4)
            f.close()


# =====================================================
# 2. phonebook using csv file (no exception handling)
# =====================================================
def phonebook_csv():
    contacts = []
    if os.path.exists(CSV_FILE):
        f = open(CSV_FILE, "r", newline="")
        reader = csv.DictReader(f)
        for row in reader:
            contacts.append({"name": row["name"], "phone": row["phone"]})
        f.close()

    while True:
        print_phonebook_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "0":
            break
        else:
            print("Wrong choice, try again")

        if choice in ["1", "4", "5"]:
            f = open(CSV_FILE, "w", newline="")
            writer = csv.DictWriter(f, fieldnames=["name", "phone"])
            writer.writeheader()
            writer.writerows(contacts)
            f.close()


# =====================================================
# 3. phonebook using binary file (no exception handling)
# =====================================================
def phonebook_binary():
    contacts = []
    if os.path.exists(BINARY_FILE):
        f = open(BINARY_FILE, "rb")
        contacts = pickle.load(f)
        f.close()

    while True:
        print_phonebook_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "0":
            break
        else:
            print("Wrong choice, try again")

        if choice in ["1", "4", "5"]:
            f = open(BINARY_FILE, "wb")
            pickle.dump(contacts, f)
            f.close()


# =====================================================
# 4. time conversion (no exception handling)
# =====================================================
def print_time_menu():
    print("\n--- TIME CONVERSION ---")
    print("1. 12 hour to 24 hour")
    print("2. 24 hour to 12 hour")
    print("3. Seconds to hh:mm:ss")
    print("4. hh:mm:ss to seconds")
    print("0. Back")


def time_conversion():
    tc = TimeConverter()

    while True:
        print_time_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            tc.set_12_hour(input("Enter time (hh:mm:ss AM/PM): "))
            print("24 hour format:", tc.get_24_hour())
        elif choice == "2":
            tc.set_24_hour(input("Enter time (hh:mm:ss): "))
            print("12 hour format:", tc.get_12_hour())
        elif choice == "3":
            tc.set_seconds(int(input("Enter seconds: ")))
            print("Time:", tc.get_24_hour())
        elif choice == "4":
            tc.set_24_hour(input("Enter time (hh:mm:ss): "))
            print("Total seconds:", tc.get_seconds())
        elif choice == "0":
            break
        else:
            print("Wrong choice, try again")


# =====================================================
# phonebook operations WITH checking (used by 5, 6, 7)
# =====================================================
def check_phone(phone):
    if not phone.isdigit() or len(phone) != 10:
        raise ValueError("Phone number must have exactly 10 digits")


def find_contact_safe(contacts, name):
    contact = find_contact(contacts, name)
    if contact is None:
        raise ValueError("Contact not found")
    return contact


def add_contact_safe(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    if name == "":
        raise ValueError("Name cannot be empty")
    check_phone(phone)
    if find_contact(contacts, name) is not None:
        raise ValueError("Contact already exists")
    contacts.append({"name": name, "phone": phone})
    print("Contact added")


def update_contact_safe(contacts):
    name = input("Enter name to update: ").strip()
    contact = find_contact_safe(contacts, name)
    phone = input("Enter new phone number: ").strip()
    check_phone(phone)
    contact["phone"] = phone
    print("Contact updated")


def delete_contact_safe(contacts):
    name = input("Enter name to delete: ").strip()
    contact = find_contact_safe(contacts, name)
    contacts.remove(contact)
    print("Contact deleted")


# =====================================================
# 5. exception handling on 1 (phonebook using json file)
# =====================================================
def phonebook_json_exception():
    contacts = []
    try:
        with open(JSON_FILE, "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        print("No json file yet, starting with an empty phonebook")
    except json.JSONDecodeError:
        print("Json file is empty or damaged, starting with an empty phonebook")
    except OSError:
        print("Error: could not read", JSON_FILE)

    while True:
        print_phonebook_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_contact_safe(contacts)
            elif choice == "2":
                view_contacts(contacts)
            elif choice == "3":
                search_contact(contacts)
            elif choice == "4":
                update_contact_safe(contacts)
            elif choice == "5":
                delete_contact_safe(contacts)
            elif choice == "0":
                break
            else:
                print("Wrong choice, try again")

            if choice in ["1", "4", "5"]:
                with open(JSON_FILE, "w") as f:
                    json.dump(contacts, f, indent=4)
        except ValueError as e:
            print("Error:", e)
        except OSError:
            print("Error: could not write to", JSON_FILE)
        except (KeyError, TypeError):
            print("Error: the phonebook file has wrong data")
            break


# =====================================================
# 6. exception handling on 2 (phonebook using csv file)
# =====================================================
def phonebook_csv_exception():
    contacts = []
    try:
        with open(CSV_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                contacts.append({"name": row["name"], "phone": row["phone"]})
    except FileNotFoundError:
        print("No csv file yet, starting with an empty phonebook")
    except KeyError:
        print("Csv file is damaged, starting with an empty phonebook")
        contacts = []
    except OSError:
        print("Error: could not read", CSV_FILE)

    while True:
        print_phonebook_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_contact_safe(contacts)
            elif choice == "2":
                view_contacts(contacts)
            elif choice == "3":
                search_contact(contacts)
            elif choice == "4":
                update_contact_safe(contacts)
            elif choice == "5":
                delete_contact_safe(contacts)
            elif choice == "0":
                break
            else:
                print("Wrong choice, try again")

            if choice in ["1", "4", "5"]:
                with open(CSV_FILE, "w", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=["name", "phone"])
                    writer.writeheader()
                    writer.writerows(contacts)
        except ValueError as e:
            print("Error:", e)
        except OSError:
            print("Error: could not write to", CSV_FILE)
        except (KeyError, TypeError):
            print("Error: the phonebook file has wrong data")
            break


# =====================================================
# 7. exception handling on 3 (phonebook using binary file)
# =====================================================
def phonebook_binary_exception():
    contacts = []
    try:
        with open(BINARY_FILE, "rb") as f:
            contacts = pickle.load(f)
    except FileNotFoundError:
        print("No binary file yet, starting with an empty phonebook")
    except (EOFError, pickle.UnpicklingError):
        print("Binary file is empty or damaged, starting with an empty phonebook")
    except OSError:
        print("Error: could not read", BINARY_FILE)

    while True:
        print_phonebook_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_contact_safe(contacts)
            elif choice == "2":
                view_contacts(contacts)
            elif choice == "3":
                search_contact(contacts)
            elif choice == "4":
                update_contact_safe(contacts)
            elif choice == "5":
                delete_contact_safe(contacts)
            elif choice == "0":
                break
            else:
                print("Wrong choice, try again")

            if choice in ["1", "4", "5"]:
                with open(BINARY_FILE, "wb") as f:
                    pickle.dump(contacts, f)
        except ValueError as e:
            print("Error:", e)
        except OSError:
            print("Error: could not write to", BINARY_FILE)
        except (KeyError, TypeError):
            print("Error: the phonebook file has wrong data")
            break


# =====================================================
# 8. exception handling on 4 (time conversion)
# =====================================================
def time_conversion_exception():
    tc = TimeConverter()

    while True:
        print_time_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                tc.set_12_hour(input("Enter time (hh:mm:ss AM/PM): "))
                print("24 hour format:", tc.get_24_hour())
            elif choice == "2":
                tc.set_24_hour(input("Enter time (hh:mm:ss): "))
                print("12 hour format:", tc.get_12_hour())
            elif choice == "3":
                tc.set_seconds(int(input("Enter seconds: ")))
                print("Time:", tc.get_24_hour())
            elif choice == "4":
                tc.set_24_hour(input("Enter time (hh:mm:ss): "))
                print("Total seconds:", tc.get_seconds())
            elif choice == "0":
                break
            else:
                print("Wrong choice, try again")
        except ValueError as e:
            print("Error:", e)


# =====================================================
# MAIN MENU
# =====================================================
while True:
    print("\n========== MAIN MENU ==========")
    print("1. Phonebook using JSON file")
    print("2. Phonebook using CSV file")
    print("3. Phonebook using Binary file")
    print("4. Time conversion")
    print("5. Phonebook using JSON file (with exception handling)")
    print("6. Phonebook using CSV file (with exception handling)")
    print("7. Phonebook using Binary file (with exception handling)")
    print("8. Time conversion (with exception handling)")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        phonebook_json()
    elif choice == "2":
        phonebook_csv()
    elif choice == "3":
        phonebook_binary()
    elif choice == "4":
        time_conversion()
    elif choice == "5":
        phonebook_json_exception()
    elif choice == "6":
        phonebook_csv_exception()
    elif choice == "7":
        phonebook_binary_exception()
    elif choice == "8":
        time_conversion_exception()
    elif choice == "0":
        print("Bye")
        break
    else:
        print("Wrong choice, try again")
