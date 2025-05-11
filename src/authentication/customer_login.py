import uuid
import json
import getpass
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
customer_file_path = os.path.join(base_dir, '..', 'database', 'customer_data.json')

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

def is_valid_email(email):
    return "@" in email and email.endswith(".com") and not email.isdigit()

def is_valid_address(address):
    return all(c.isalnum() or c.isspace() for c in address)

def load_customers():
    if not os.path.exists(customer_file_path):
        return []
    with open(customer_file_path, "r") as file:
        return json.load(file)

def save_customer(customer):
    customers = load_customers()
    customers.append(customer)
    with open(customer_file_path, "w") as file:
        json.dump(customers, file, indent=4)

def customer_signup():
    print("\n---- customer sign up ----")
    customer_id = str(uuid.uuid4())[:6]

    name = input("enter customer name: ")
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
        if strength == 1:
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

    customer_data = {
        "id": customer_id,
        "name": name,
        "email": email,
        "password": password,
        "contact": contact,
        "address": address
    }

    save_customer(customer_data)
    print("customer registered successfully!\n")

def customer_login():
    print("\n---- customer login ----")
    customers = load_customers()
    
    if len(customers) == 0:
        print("no records found! please sign up first.\n")
        return False

    while True:
        email = input("enter email:- ")
        password = getpass.getpass("enter password:- ")

        login_successful = False
        for customer in customers:
            if customer["email"] == email and customer["password"] == password:
                print(f"login successful! welcome, {customer['name']}")
                login_successful = True
                break
        
        if login_successful:
            return True
        print("invalid email or password! please try again.\n")
