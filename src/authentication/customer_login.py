import json
import uuid
import getpass
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
customer_file_path = os.path.join(base_dir, '..', 'database', 'customers.json')

def is_valid_name(name):
    return name.replace(" ", "").isalpha()

def is_valid_contact(contact):
    if not contact.isdigit() or len(contact) != 10:
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
    if not os.path.exists(customer_file_path) or os.path.getsize(customer_file_path) == 0:
        return []
    with open(customer_file_path, "r") as file:
        return json.load(file)

def save_customer(customer):
    customers = load_customers()
    customers.append(customer)
    with open(customer_file_path, "w") as file:
        json.dump(customers, file, indent=4)

def customer_signup():
    print("\n---- Customer Sign Up ----")
    customer_id = str(uuid.uuid4())[:6]

    name = input("Enter customer name: ")
    if not is_valid_name(name):
        print("Invalid name! Only letters are allowed.")
        return

    email = input("Enter email: ")
    if not is_valid_email(email):
        print("Invalid email! Must contain '@' and end with '.com' and not be all digits.")
        return

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
    print("Customer registered successfully!\n")


def customer_login():
    print("\n---- Customer Login ----")
    customers = load_customers()
    
    if len(customers) == 0:
        print("No records found! Please sign up first.\n")
        return False

    while True:
        email = input("Enter email: ")
        password = getpass.getpass("Enter password: ")

        for customer in customers:
            if customer["email"] == email and customer["password"] == password:
                print(f"Login successful! Welcome, {customer['name']}")
                
                return True
        
        print("Invalid email or password! Please try again.\n")

def customer_auth_menu():
    while True:
        print("\n--- Customer dashboard ---")
        print("1. Sign Up")
        print("2. Login")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            customer_signup()
        elif choice == "2":
            logged_in = customer_login()
            if logged_in:
                continue 
        elif choice == "3":
            print("Returning to main menu...\n")
            break
        else:
            print("Invalid choice! Try again.\n")
