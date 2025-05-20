import json
import uuid
from datetime import datetime

def load_orders():
    try:
        with open('src/database/order_records.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def load_menu():
    try:
        with open('src/database/menu_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_bill(bill_data):
    try:
        with open('src/database/bills.json', 'r') as file:
            all_bills = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        all_bills = []

    all_bills.append(bill_data)
    with open('src/database/bills.json', 'w') as file:
        json.dump(all_bills, file, indent=4)

def generate_bill(customer_id):
    orders = load_orders()
    menu = load_menu()
    
    customer_orders = [order for order in orders if order['customer_id'] == customer_id]
    if not customer_orders:
        print("No orders found for this customer.")
        return

    total = 0
    print("\n---- BILL DETAILS ----")

    for order in customer_orders:
        print(f"\nOrder ID: {order['order_id']}  Date: {order['datetime']}")
        for item in order['items']:
            item_id = item['item_id']
            quantity = item['quantity']

            found_item = None
            for category in menu:
                for menu_item in menu[category]:
                    if menu_item['item_id'] == item_id:
                        found_item = menu_item
                        break
                if found_item:
                    break

            if found_item:
                name = found_item['name'] 
                price = found_item['price']
                item_total = price * quantity
                print(f"{name} x {quantity} = ₹{item_total}")
                total += item_total
            else:
                print(f"Item ID {item_id} not found in menu.")

    gst = round(total * 0.05, 2)
    grand_total = round(total + gst, 2)

    print(f"\nSubtotal: ₹{total}")
    print(f"GST (5%): ₹{gst}")
    print(f"Total Amount Payable: ₹{grand_total}")

    bill_data = {
        "bill_id": str(uuid.uuid4()),
        "customer_id": customer_id,
        "orders": customer_orders,
        "subtotal": total,
        "gst": gst,
        "grand_total": grand_total,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    save_bill(bill_data)
    print("\nBill generated and saved successfully!")


