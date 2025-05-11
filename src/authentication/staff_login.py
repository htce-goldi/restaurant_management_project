import uuid
import json
import getpass
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
staff_file_path = os.path.join(base_dir, '..', 'database', 'staff_data.json')

def is_valid_name(name):
    return name.replace(" ", "").isalpha()

def is_valid_contact(contact):
    if not contact.isdigit():
        return False
    if len(set(contact)) == 1:
        return False
    for digit in set(contact):
        if contact.count(digit) >= 5:
            return False
    return True

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

def load_staff():
    if not os.path.exists(staff_file_path):
        return []
    with open(staff_file_path, "r") as file:
        return json.load(file)

def save_staff(staff):
    staff_list = load_staff()
    staff_list.append(staff)
    with open(staff_file_path, "w") as file:
        json.dump(staff_list, file, indent=4)

def staff_signup():
    print("\n--- staff sign up ---")
    staff_id = str(uuid.uuid4())[:6]

    name = input("enter staff name:- ")
    if not is_valid_name(name):
        print("invalid name! only letters are allowed.")
        return

    while True:
        contact = input("enter contact number:- ")
        if is_valid_contact(contact):
            break
        else:
            print("invalid contact! only digits allowed, digits must not all be same, and no digit should repeat 5+ times.")

    while True:
        password = getpass.getpass("create a password:- ")
        strength = check_password_strength(password)
        if strength == 1:
            print("weak password! use at least two types: letters, numbers, special characters.")
        else:
            break

    role = input("enter your role (e.g. waiter, chef):- ")

    staff_data = {
        "id": staff_id,
        "name": name,
        "contact": contact,
        "password": password,
        "role": role
    }

    save_staff(staff_data)
    print("staff registered successfully!\n")

def staff_login():
    print("\n---- staff login ----")
    staff_list = load_staff()

    if len(staff_list) == 0:
        print("no records found! please sign up first.\n")
        return False
    
    while True:
        contact = input("enter contact number: ")
        password = getpass.getpass("enter your password:- ")

        login_successful = False
        for staff in staff_list:
            if staff["contact"] == contact and staff["password"] == password:
                print(f"login successful! welcome, {staff['name']}")
                login_successful = True
                break
        
        if login_successful:
            return True
        print("invalid contact or password! please try again.\n")
