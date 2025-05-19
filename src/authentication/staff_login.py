import json
import uuid
import getpass
import os
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))
staff_file_path = os.path.join(base_dir, '..', 'database', 'staff.json')

def is_valid_name(name):
    return name.replace(" ", "").isalpha()

def is_valid_email(email):
    return "@" in email and email.endswith(".com")

def is_valid_contact(contact):
    return (
        contact.isdigit() and 
        len(contact) == 10 and 
        len(set(contact)) != 1 and 
        all(contact.count(d) < 5 for d in set(contact))
    )

def check_password_strength(password):
    has_letter = False
    has_digit = False
    has_special = False

    for c in password:
        if c.isalpha():
            has_letter = True
        elif c.isdigit():
            has_digit = True
        elif not c.isalnum():
            has_special = True

    
        if (has_letter + has_digit + has_special) >= 2:
            return True

    return (has_letter + has_digit + has_special) >= 2

def load_staff():
    if not os.path.exists(staff_file_path) or os.path.getsize(staff_file_path) == 0:
        return []
    with open(staff_file_path, "r") as file:
        return json.load(file)

def save_staff(staff_list):
    with open(staff_file_path, "w") as file:
        json.dump(staff_list, file, indent=4)


def staff_signup():
    print("\n---- Staff Sign Up ----")

    name = input("Enter name: ")
    if not is_valid_name(name):
        print("Invalid name! Only letters allowed.")
        return

    email = input("Enter email: ")
    if not is_valid_email(email):
        print("Invalid email! Must contain '@' and end with '.com'.")
        return

    all_staff = load_staff()
    if any(staff["email"] == email for staff in all_staff):
        print("Email already registered. Please login.")
        return

    while True:
        password = getpass.getpass("Create a password: ")
        if check_password_strength(password):
            break
        print("Weak password! Use a mix of letters, numbers, and symbols.")

    contact = input("Enter contact number: ")
    if not is_valid_contact(contact):
        print("Invalid contact number! Must be 10 digits and not all same.")
        return

    role = input("Enter role (e.g., waiter, chef): ").strip()

    staff_data = {
        "id": str(uuid.uuid4())[:8],
        "name": name,
        "email": email,
        "password": password,
        "contact": contact,
        "role": role,
        "date_joined": datetime.now().strftime("%Y-%m-%d")
    }

    all_staff.append(staff_data)
    save_staff(all_staff)
    print("Staff registered successfully!\n")

def staff_login():
    print("\n---- Staff Login ----")
    all_staff = load_staff()

    if not all_staff:
        print("No staff records found. Please sign up first.\n")
        return None

    email = input("Enter email: ")
    password = getpass.getpass("Enter password: ")

    for staff in all_staff:
        if staff["email"] == email and staff["password"] == password:
            print(f"Login successful! Welcome, {staff['name']}")
            return staff["role"]

    print("Invalid email or password.\n")
    return None

def staff_auth_menu():
    while True:
        print("\n--- Staff Authentication ---")
        print("1. Sign Up")
        print("2. Login")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            staff_signup()
        elif choice == '2':
            role = staff_login()
            if role:
                return role  
        elif choice == '3':
            print("Returning to main menu...\n")
            return None
        else:
            print("Invalid choice! Please try again.\n")
