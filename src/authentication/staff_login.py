import json
import os
import uuid

class staffmanager:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, '..', 'database', 'staff_data.json')


    @staticmethod
    def read_staff():
        if not os.path.exists(staffmanager.path) or os.path.getsize(staffmanager.path) == 0:
            return []
        with open(staffmanager.path, 'r') as f:
            return json.load(f)

    @staticmethod
    def write_staff(data):
        with open(staffmanager.path, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def register_staff(cls):
        staff_name = input("enter staff name: ")
        staff_address = input("enter address: ")
        staff_contact = input("enter contact number: ")
        staff_id = str(uuid.uuid4())[:6]

        staff = {
            "staff_id": staff_id,
            "name": staff_name,
            "address": staff_address,
            "contact": staff_contact,
            "role": None
        }
        staff_list = cls.read_staff()
        staff_list.append(staff)
        cls.write_staff(staff_list)
        print(f"staff '{staff_name}' registered successfully!")

    @classmethod
    def staff_login(cls):
        staff_name = input("enter your name: ")
        staff_contact = input("enter your contact number: ")

        staff_list = cls.read_staff()
        for staff in staff_list:
            if staff["name"] == staff_name and staff["contact"] == staff_contact:
                print(f"welcome {staff_name}, login successful!")
                print("role:", staff.get("role", "not assigned"))

                if staff["role"] is None:
                    staff["role"] = "staff"  

                cls.write_staff(staff_list)  
                return True
        print("login failed. incorrect details.")
        return False

    @classmethod
    def list_staff(cls):
        staff_list = cls.read_staff()
        if not staff_list:
            print("no staff records found.")
            return
        print("staff members:")
        for staff in staff_list:
            print(f"id: {staff['staff_id']}, name: {staff['name']}, contact: {staff['contact']}, role: {staff.get('role', 'n/a')}")
