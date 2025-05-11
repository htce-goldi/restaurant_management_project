import uuid
import json
import getpass
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
admin_file_path = os.path.join(base_dir, '..', 'database', 'admin_data.json')

def is_valid_name(name):
    return name.replace(" ", "").isalpha()

def is_valid_email(email):
    return "@" in email and email.endswith(".com") and not email.isdigit()

def is_valid_contact(contact):
    if not contact.isdigit():
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
    print("\n---- admin sign up ----")
    admin_id = str(uuid.uuid4())[:6]

    name = input("enter admin name:- ")
    if not is_valid_name(name):
        print("invalid name! only letters are allowed.")
        return

    email = input("enter email:- ")
    if not is_valid_email(email):
        print("invalid email! must contain '@.com' and not be all digits.")
        return

    while True:
        password = getpass.getpass("create a password:- ")
        strength = check_password_strength(password)
        if strength < 2:
            print("weak password! use at least two types: letters, numbers, special characters.")
        else:
            break

    while True:
        contact = input("enter contact number:- ")
        if is_valid_contact(contact):
            break
        else:
            print("invalid contact! only digits allowed, digits must not all be same, and no digit should repeat 5+ times.")

    address = input("enter address:- ")
    if not is_valid_address(address):
        print("invalid address! no special characters allowed.")
        return

    admin_data = {
        "id": admin_id,
        "name": name,
        "email": email,
        "password": password,
        "contact": contact,
        "address": address
    }

    save_admin(admin_data)
    print("admin registered successfully!\n")

def admin_login():
    print("\n---- admin login ----")
    
    if not os.path.exists(admin_file_path) or os.path.getsize(admin_file_path) == 0:
        print("no records found! please sign up first.\n")
        return False

    email = input("enter email:- ")
    password = getpass.getpass("enter password:- ")

    admins = load_admins()
    
    for admin in admins:
        if admin["email"] == email:
            if admin["password"] == password:
                print(f"login successful! welcome, {admin['name']}")
                return True
    
    print("invalid email or password!\n")
    return False
