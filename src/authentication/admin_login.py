import json
import uuid
import getpass
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
admin_file_path = os.path.join(base_dir, '..', 'database', 'admin.json')

def is_valid_name(name):
    return name.replace(" ", "").isalpha()

def is_valid_email(email):
    return "@" in email and email.endswith(".com") and not email.isdigit()

def is_valid_contact(contact):
    if not contact.isdigit() or len(contact) != 10:
        return False
    if len(set(contact)) == 1:
        return False
    for digit in set(contact):
        if contact.count(digit) >= 5:
            return False
    return True

def is_valid_address(address):
    return all(c.isalnum() or c.isspace() for c in address)

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

    strength = 0
    if has_letter:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    return strength

def load_admins():
    if not os.path.exists(admin_file_path) or os.path.getsize(admin_file_path) == 0:
        return []
    with open(admin_file_path, "r") as file:
        return json.load(file)

def save_admin(admin):
    admins = load_admins()
    admins.append(admin)
    with open(admin_file_path, "w") as file:
        json.dump(admins, file, indent=4)

def admin_signup():
    admins = load_admins()
    if admins:
        print("Admin already registered! Only one admin allowed.\n")
        return False  # Signup not allowed

    print("\n---- Admin Sign Up ----")
    admin_id = str(uuid.uuid4())[:6]

    name = input("Enter admin name: ")
    if not is_valid_name(name):
        print("Invalid name! Only letters are allowed.")
        return False

    email = input("Enter email: ")
    if not is_valid_email(email):
        print("Invalid email! Must contain '@' and end with '.com' and not be all digits.")
        return False

    while True:
        password = getpass.getpass("Create a password: ")
        strength = check_password_strength(password)
        if strength < 2:
            print("Weak password! Use at least two types: letters, numbers, special characters.")
        else:
            break

    while True:
        contact = input("Enter contact number: ")
        if is_valid_contact(contact):
            break
        else:
            print("Invalid contact! Must be 10 digits, not all same, and no digit repeated 5+ times.")

    address = input("Enter address: ")
    if not is_valid_address(address):
        print("Invalid address! No special characters allowed.")
        return False

    admin_data = {
        "id": admin_id,
        "name": name,
        "email": email,
        "password": password,
        "contact": contact,
        "address": address
    }

    save_admin(admin_data)
    print("Admin registered successfully!\n")
    return True

def admin_login():
    print("\n---- Admin Login ----")

    admins = load_admins()
    if not admins:
        print("No admin registered yet! Please sign up first.\n")
        return False

    email = input("Enter email: ")
    password = getpass.getpass("Enter password: ")

    for admin in admins:
        if admin["email"] == email and admin["password"] == password:
            print(f"Login successful! Welcome, {admin['name']}")
           
            return True

    print("Invalid email or password!\n")
    return False


def admin_auth_menu():
    while True:
        admins = load_admins()
        print("\n--- Admin Authentication ---")
        if admins:
         
            print("1. Login")
            print("2. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                if admin_login():
                    print("You have logged out from admin panel.\n")
            elif choice == "2":
                print("Returning to main menu...\n")
                break
            else:
                print("Invalid choice! Try again.\n")
        else:
          
            print("1. Sign Up (Only one admin allowed)")
            print("2. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                if admin_signup():
                    print("Please login now.\n")
                else:
                    print("Signup failed or admin already exists.\n")
            elif choice == "2":
                print("Returning to main menu...\n")
                break
            else:
                print("Invalid choice! Try again.\n")
