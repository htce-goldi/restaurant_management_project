import json
import os
import uuid

class adminmanager:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    admin_file = os.path.join(base_dir, '..', 'database', 'admin_data.json')

    @staticmethod
    def read_json(file_path):
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return []
        with open(file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def write_json(file_path, data):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def register_admin(cls):
        print("\n--- register admin ---")
        admin_name = input("admin name:- ")
        admin_address = input("enter your address:- ")
        admin_contact = input("enter your contact number:- ")

        if not admin_contact.isdigit() or len(admin_contact) != 10:
            print("invalid contact number. must be exactly 10 digits.")
            return

        admin_id = str(uuid.uuid4())[:6]

        admin = {
            "admin_id": admin_id,
            "name": admin_name,
            "address": admin_address,
            "contact": admin_contact
        }

        admin_list = cls.read_json(cls.admin_file)
        admin_list.append(admin)
        cls.write_json(cls.admin_file, admin_list)
        print("admin registered successfully.\n")

    @classmethod
    def admin_login(cls):
        print("\n--- admin login ---")
        name = input("enter your name: ")
        contact = input("enter your contact number: ")

        admins = cls.read_json(cls.admin_file)
        for admin in admins:
            if admin["name"] == name and admin["contact"] == contact:
                print("login successful.\n")
                return True
        print("login failed.\n")
        return False

    @classmethod
    def show_all_admins(cls):
        print("\n--- registered admins ---")
        admins = cls.read_json(cls.admin_file)
        if not admins:
            print("no admin records found.\n")
        else:
            for admin in admins:
                print("id:", admin["admin_id"])
                print("name:", admin["name"])
                print("contact:", admin["contact"])
                print("-" * 30)

    @classmethod
    def assign_staff_role(cls):
        print("\n--- assign role to staff ---")
        staff_data = cls.read_json(cls.staff_file)
        if not staff_data:
            print("no staff available to assign role.\n")
            return

        print("available staff members:")
        for count, staff in enumerate(staff_data, start=1):
            print(str(count) + ". " + staff["name"] + " (id: " + staff["staff_id"] + ")")

        try:
            option = int(input("choose staff number to assign role: ")) - 1
            if 0 <= option < len(staff_data):
                role = input("enter role (e.g., manager, chef): ")
                staff_data[option]["role"] = role
                cls.write_json(cls.staff_file, staff_data)
                print("role assigned successfully.\n")
            else:
                print("invalid staff selection.\n")
        except ValueError:
            print("invalid input. please enter a number.\n")
