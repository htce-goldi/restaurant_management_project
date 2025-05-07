import json
import os
import uuid

class customermanager:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, '..', 'database', 'customer_data.json')


    @staticmethod
    def read_customers():
        if not os.path.exists(customermanager.path) or os.path.getsize(customermanager.path) == 0:
            return []
        with open(customermanager.path, 'r') as f:
            return json.load(f)

    @staticmethod
    def write_customers(data):
        with open(customermanager.path, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def register_customer(cls):
        customer_name = input("enter customer Name:- ")
        customer_phone = input("enter mobile Number:- ")
        customer_address = input("enter address:- ")
        customer_id = str(uuid.uuid4())[:6]

        customer = {
            "customer_id": customer_id,
            "name": customer_name,
            "phone": customer_phone,
            "address": customer_address
        }

        data = cls.read_customers()
        data.append(customer)
        cls.write_customers(data)
        print(f"customer '{customer_name}' registered successfully!")

    @classmethod
    def customer_login(cls):
        customer_name = input("enter your name:- ")
        customer_phone = input("enter your mobile number:- ")

        data = cls.read_customers()
        for customer in data:
            if customer["name"] == customer_name and customer["phone"] == customer_phone:
                print(f"welcome {customer_name}, login successful!")
                return True
        print("login failed! incorrect credentials.")
        return False

    @classmethod
    def show_customers(cls):
        customers = cls.read_customers()
        if not customers:
            print("no customers found.")
        else:
            print("customer List:- ")
            for customer in customers:
                print(f"id: {customer['customer_id']}, name: {customer['name']}, phone: {customer['phone']}")