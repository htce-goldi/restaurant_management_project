import json
import uuid
from datetime import datetime
import os

# Paths to JSON files
menu_file = "src/database/menu_data.json"
order_file = "src/database/order_records.json"

# Check and create menu file if not exists
if not os.path.exists(menu_file):
    with open(menu_file, "w") as f:
        json.dump({}, f)

# Check and create order file if not exists
if not os.path.exists(order_file):
    with open(order_file, "w") as f:
        json.dump([], f)

def load_menu_data():
    """Load the menu data from the menu_data.json file."""
    try:
        with open(menu_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Menu data file not found.")
        return {}

def save_order(order):
    """Save an order to the order_records.json file."""
    try:
        with open(order_file, "r") as f:
            all_orders = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        all_orders = []

    all_orders.append(order)
    with open(order_file, "w") as f:
        json.dump(all_orders, f, indent=4)

def update_stock(item_id, quantity):
    """Update the stock after an order is placed."""
    menu = load_menu_data()
    if not menu:
        print("Menu is empty, can't process order.")
        return

    for category, items in menu.items():
        for item in items:
            if item["item_id"] == item_id:
                if item["stock"] >= quantity:
                    item["stock"] -= quantity
                    print(f"Stock updated for {item['name']} by {quantity}")
                else:
                    print(f"Not enough stock for {item['name']}. Available: {item['stock']}")
                    return
    
    with open(menu_file, "w") as f:
        json.dump(menu, f, indent=4)

def place_order(customer_id):
    """Main function to place an order."""
    menu = load_menu_data()
    if not menu:
        print("Menu is empty. Cannot place order.")
        return 

    cart = []
    total_amount = 0

    while True:
        print("\n--- MENU CATEGORIES ---")
        for category in menu:
            print(f"- {category.title()}")

        category_choice = input("Enter category: ").lower()
        if category_choice not in menu:
            print("Invalid category! Please choose a valid category.")
            continue

        print(f"\n--- ITEMS IN {category_choice.upper()} ---")
        for item in menu[category_choice]:
            print(f"{item['item_id']} | {item['name']} | ₹{item['price']} | Stock: {item['stock']}")

        item_id = input("Enter item ID to order: ")
        item_found = None
        for item in menu[category_choice]:
            if item["item_id"] == item_id:
                item_found = item
                break

        if not item_found:
            print("Item ID not found in this category.")
            continue

        if item_found["stock"] <= 0:
            print("This item is out of stock.")
            continue

        try:
            qty = int(input("Enter quantity: "))
            if qty <= 0:
                print("Quantity must be a positive number.")
                continue
            if qty > item_found["stock"]:
                print(f"Only {item_found['stock']} left in stock.")
                continue
        except ValueError:
            print("Quantity must be a valid number.")
            continue

        cart.append({
            "item_id": item_found["item_id"],
            "name": item_found["name"],
            "price": item_found["price"],
            "quantity": qty,
            "subtotal": item_found["price"] * qty
        })

        total_amount += item_found["price"] * qty
        update_stock(item_found["item_id"], qty)
        print(f"Added {qty} x {item_found['name']} to cart.")

        cont = input("Do you want to order more? (yes/no): ").lower()
        if cont != "yes":
            break

    if cart:
        order_data = {
            "order_id": str(uuid.uuid4()),
            "customer_id": customer_id,
            "items": cart,
            "total_amount": total_amount,
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        save_order(order_data)

        print("\nOrder placed successfully!")
        print(" --- ORDER SUMMARY ---")
        for item in cart:
            print(f"{item['name']} x {item['quantity']} = ₹{item['subtotal']}")
        print(f"TOTAL = ₹{total_amount}")
        
        # Call payment function
        payment_method = process_payment(total_amount)
        print(f"Payment Method Selected: {payment_method}")
    else:
        print("No items were ordered.")

def view_all_orders():
    """View all orders that have been placed."""
    try:
        with open(order_file, "r") as f:
            orders = json.load(f)
    except FileNotFoundError:
        print("No orders file found.")
        return
    except json.JSONDecodeError:
        print("Order records file is corrupted.")
        return

    if not orders:
        print("No orders found.")
        return

    print("\n--- ALL ORDERS ---")
    for order in orders:
        print(f"\nOrder ID: {order['order_id']}")
        print(f"Customer ID: {order['customer_id']}")
        print(f"Date & Time: {order['datetime']}")
        for item in order["items"]:
            print(f"  - {item['name']} x {item['quantity']} = ₹{item['subtotal']}")
        print(f"Total: ₹{order['total_amount']}")

# Payment Process Function
def process_payment(total):
    print(f"Total to pay: ₹{total}")
    
    # Providing payment options (you can enhance this for real payments)
    payment_method = input("Select payment method:\n1. Credit/Debit Card\n2. Cash on Delivery\n3. PayPal\nEnter your choice: ")
    
    if payment_method == '1':
        print("Payment via Credit/Debit Card is being processed...")
        return "Credit/Debit Card"
    elif payment_method == '2':
        print("Cash on Delivery selected. Order will be delivered soon!")
        return "Cash on Delivery"
    elif payment_method == '3':
        print("Payment via PayPal is being processed...")
        return "PayPal"
    else:
        print("Invalid payment method. Please try again.")
        return "Invalid"

# Importing menu management functions
from domain.menu_management import get_menu_items, menu_management_dashboard

# Order Processing Dashboard for Customers
def order_processing_dashboard(customer_id):
    """Order processing and payment"""
    print("\n--- Order Processing ---")

    # Local import to avoid circular imports
    from domain.menu_management import get_menu_items

    menu_items = get_menu_items()  # Fetching menu items from the menu management
    if not menu_items:
        print("Menu is currently empty.")
        return

    print("Available Menu Items:")
    for index, item in enumerate(menu_items, start=1):
        print(f"{index}. {item['name']} - ₹{item['price']}")
    
    # ... (rest of the order processing code)

def customer_dashboard(customer_id):
    while True:
        print("\n--- Customer Dashboard ---")
        print("1. View Menu")
        print("2. Place Order")
        print("3. Back to Main Menu")

        sub_choice = input("Enter your choice: ")

        if sub_choice == '1':
            # Display the menu
            menu_items = get_menu_items()
            print("\n--- Menu ---")
            for index, item in enumerate(menu_items, start=1):
                print(f"{index}. {item['name']} - ₹{item['price']}")
        elif sub_choice == '2':
            # Call the order processing dashboard for the customer
            order_processing_dashboard(customer_id)
        elif sub_choice == '3':
            break
        else:
            print("Invalid option. Please try again.")

# Main Function to Simulate the System
def menu_dashboards():
    # Simulating customer login
    customer_id = "C123"  # This would be retrieved after customer login
    print(f"Customer ID: {customer_id}")
    
    customer_dashboard(customer_id)

if __name__ == "__main__":
    menu_dashboards()
