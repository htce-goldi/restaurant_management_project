import json
import os
import uuid

base_dir = os.path.dirname(os.path.abspath(__file__))
menu_file = os.path.join(base_dir, '..', 'database', 'menu_data.json')

def load_menu():
    if not os.path.exists(menu_file):
        return {}
    try:
        with open(menu_file, 'r') as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError):
        return {}

def save_menu(menu):
    try:
        os.makedirs(os.path.dirname(menu_file), exist_ok=True)
        with open(menu_file, 'w') as file:
            json.dump(menu, file, indent=4)
    except IOError:
        print("Error saving menu data!")

def display_menu():
    menu = load_menu()
    if not menu:
        print("The menu is empty.")
        return

    print("\n====== RESTAURANT MENU ======\n")
    for category, items in menu.items():
        print(f"{category.capitalize()}:")
        print("-" * 60)
        print(f"{'ID':<8} | {'Name':<25} | {'Size':<10} | {'Price':<6} | Stock")
        print("-" * 60)
        for item in items[:5]:
            itemid = item.get("itemid", "")[:6]
            name = item.get("name", "")
            qty = item.get("qty", item.get("qty/half", "N/A"))
            price = item.get("price", item.get("qty/half", "N/A"))
            stock = item.get("stock", 0)

            if "qty/half" in item and "full" in item:
                print(f"{itemid:<8} | {name:<25} | Half     | ₹{item['qty/half']:<5} | {stock}")
                print(f"{'':<8} | {'':<25} | Full     | ₹{item['full']:<5} | {stock}")
            else:
                print(f"{itemid:<8} | {name:<25} | {qty:<10} | ₹{price:<6} | {stock}")
        print()

def add_initial_menu_items():
    menu = load_menu()
    if menu:
        print("Menu already exists.")
        return

    menu = {
        "breakfast": [
            {"itemid": "bf01", "name": "Idli Sambhar", "qty": "2 pcs", "price": 40, "stock": 30},
            {"itemid": "bf02", "name": "Masala Dosa", "qty": "1 plate", "price": 60, "stock": 20},
            {"itemid": "bf03", "name": "Poha", "qty": "1 bowl", "price": 30, "stock": 25},
            {"itemid": "bf04", "name": "Aloo Paratha", "qty": "1 plate", "price": 50, "stock": 20},
            {"itemid": "bf05", "name": "Upma", "qty": "1 bowl", "price": 35, "stock": 30},
            {"itemid": "bf06", "name": "Puri Bhaji", "qty": "1 plate", "price": 55, "stock": 20},
            {"itemid": "bf07", "name": "Egg Sandwich", "qty": "1 sandwich", "price": 45, "stock": 15},
            {"itemid": "bf08", "name": "Vegetable Cutlet", "qty": "2 pcs", "price": 40, "stock": 20},
            {"itemid": "bf09", "name": "Chole Kulche", "qty": "1 plate", "price": 60, "stock": 25},
            {"itemid": "bf10", "name": "Bread Butter", "qty": "2 slices", "price": 20, "stock": 30}
        ],
        "lunch": [
            {"itemid": "ln01", "name": "Thali Veg", "qty": "1 thali", "price": 120, "stock": 20},
            {"itemid": "ln02", "name": "Chicken Curry", "qty": "1 plate", "price": 150, "stock": 15},
            {"itemid": "ln03", "name": "Paneer Butter Masala", "qty": "1 plate", "price": 130, "stock": 15},
            {"itemid": "ln04", "name": "Veg Biryani", "qty": "1 plate", "price": 100, "stock": 20},
            {"itemid": "ln05", "name": "Dal Fry", "qty": "1 bowl", "price": 70, "stock": 25},
            {"itemid": "ln06", "name": "Roti", "qty": "1 pc", "price": 10, "stock": 100},
            {"itemid": "ln07", "name": "Jeera Rice", "qty": "1 plate", "price": 80, "stock": 20},
            {"itemid": "ln08", "name": "Mix Veg", "qty": "1 plate", "price": 90, "stock": 20},
            {"itemid": "ln09", "name": "Fish Curry", "qty": "1 plate", "price": 160, "stock": 10},
            {"itemid": "ln10", "name": "Curd", "qty": "1 bowl", "price": 25, "stock": 25}
        ],
        "dinner": [
            {"itemid": "dn01", "name": "Butter Naan", "qty": "1 pc", "price": 20, "stock": 50},
            {"itemid": "dn02", "name": "Chicken Biryani", "qty": "1 plate", "price": 160, "stock": 15},
            {"itemid": "dn03", "name": "Paneer Tikka", "qty": "6 pcs", "price": 140, "stock": 10},
            {"itemid": "dn04", "name": "Kadhai Chicken", "qty": "1 plate", "price": 170, "stock": 12},
            {"itemid": "dn05", "name": "Tandoori Roti", "qty": "1 pc", "price": 15, "stock": 50},
            {"itemid": "dn06", "name": "Dal Makhani", "qty": "1 bowl", "price": 90, "stock": 20},
            {"itemid": "dn07", "name": "Malai Kofta", "qty": "1 plate", "price": 110, "stock": 10},
            {"itemid": "dn08", "name": "Egg Curry", "qty": "1 plate", "price": 100, "stock": 15},
            {"itemid": "dn09", "name": "Veg Kofta", "qty": "1 plate", "price": 95, "stock": 15},
            {"itemid": "dn10", "name": "Fried Rice", "qty": "1 plate", "price": 90, "stock": 20}
        ],
        "snacks": [
            {"itemid": "sn01", "name": "Samosa", "qty": "1 pc", "price": 15, "stock": 50},
            {"itemid": "sn02", "name": "Pakora", "qty": "1 plate", "price": 40, "stock": 30},
            {"itemid": "sn03", "name": "French Fries", "qty": "1 plate", "price": 60, "stock": 25},
            {"itemid": "sn04", "name": "Veg Puff", "qty": "1 pc", "price": 20, "stock": 30},
            {"itemid": "sn05", "name": "Spring Roll", "qty": "2 pcs", "price": 50, "stock": 20},
            {"itemid": "sn06", "name": "Aloo Tikki", "qty": "1 pc", "price": 25, "stock": 30},
            {"itemid": "sn07", "name": "Cheese Balls", "qty": "5 pcs", "price": 70, "stock": 15},
            {"itemid": "sn08", "name": "Cutlet", "qty": "1 pc", "price": 30, "stock": 25},
            {"itemid": "sn09", "name": "Nachos", "qty": "1 bowl", "price": 60, "stock": 20},
            {"itemid": "sn10", "name": "Bread Pakora", "qty": "1 pc", "price": 20, "stock": 25}
        ],
        "drinks": [
            {"itemid": "dr01", "name": "Lassi", "qty": "1 glass", "price": 40, "stock": 20},
            {"itemid": "dr02", "name": "Cold Coffee", "qty": "1 glass", "price": 50, "stock": 20},
            {"itemid": "dr03", "name": "Tea", "qty": "1 cup", "price": 15, "stock": 40},
            {"itemid": "dr04", "name": "Coffee", "qty": "1 cup", "price": 20, "stock": 40},
            {"itemid": "dr05", "name": "Buttermilk", "qty": "1 glass", "price": 25, "stock": 30},
            {"itemid": "dr06", "name": "Mango Shake", "qty": "1 glass", "price": 60, "stock": 15},
            {"itemid": "dr07", "name": "Banana Shake", "qty": "1 glass", "price": 55, "stock": 15},
            {"itemid": "dr08", "name": "Rose Milk", "qty": "1 glass", "price": 45, "stock": 20},
            {"itemid": "dr09", "name": "Water Bottle", "qty": "500ml", "price": 20, "stock": 50},
            {"itemid": "dr10", "name": "Masala Soda", "qty": "1 glass", "price": 30, "stock": 25}
        ],
        "soft drinks": [
            {"itemid": "sd01", "name": "Coca Cola", "qty": "250ml", "price": 25, "stock": 40},
            {"itemid": "sd02", "name": "Pepsi", "qty": "250ml", "price": 25, "stock": 40},
            {"itemid": "sd03", "name": "Sprite", "qty": "250ml", "price": 25, "stock": 35},
            {"itemid": "sd04", "name": "Fanta", "qty": "250ml", "price": 25, "stock": 35},
            {"itemid": "sd05", "name": "Thumbs Up", "qty": "250ml", "price": 25, "stock": 30},
            {"itemid": "sd06", "name": "7UP", "qty": "250ml", "price": 25, "stock": 30},
            {"itemid": "sd07", "name": "Limca", "qty": "250ml", "price": 25, "stock": 25},
            {"itemid": "sd08", "name": "Appy Fizz", "qty": "250ml", "price": 30, "stock": 20},
            {"itemid": "sd09", "name": "Mountain Dew", "qty": "250ml", "price": 25, "stock": 25},
            {"itemid": "sd10", "name": "Slice", "qty": "250ml", "price": 25, "stock": 25}
        ],
        "desserts": [
            {"itemid": "ds01", "name": "Gulab Jamun", "qty": "2 pcs", "price": 40, "stock": 20},
            {"itemid": "ds02", "name": "Rasgulla", "qty": "2 pcs", "price": 40, "stock": 20},
            {"itemid": "ds03", "name": "Ice Cream", "qty": "1 scoop", "price": 30, "stock": 30},
            {"itemid": "ds04", "name": "Brownie", "qty": "1 pc", "price": 50, "stock": 15},
            {"itemid": "ds05", "name": "Cake Slice", "qty": "1 slice", "price": 40, "stock": 20},
            {"itemid": "ds06", "name": "Kheer", "qty": "1 bowl", "price": 35, "stock": 15},
            {"itemid": "ds07", "name": "Halwa", "qty": "1 bowl", "price": 30, "stock": 15},
            {"itemid": "ds08", "name": "Custard", "qty": "1 bowl", "price": 30, "stock": 15},
            {"itemid": "ds09", "name": "Fruit Salad", "qty": "1 bowl", "price": 45, "stock": 15},
            {"itemid": "ds10", "name": "Chocolate Mousse", "qty": "1 cup", "price": 55, "stock": 10}
        ]
    }
    save_menu(menu)
    print("Initial menu items added successfully.")

# Placeholder functions to be implemented later
def add_new_menu_item():
    print("Function to add new item not implemented yet.")

def update_stock():
    print("Function to update stock not implemented yet.")

def menu_management(role):
    if role.lower() == "admin":
        return {
            "add_initial_items": add_initial_menu_items,
            "display_menu": display_menu,
            "add_new_item": add_new_menu_item,
            "update_stock": update_stock
        }
    else:
        return {
            "display_menu": display_menu
        }

def menu_management_dashboard(role, menu_functions):
    while True:
        print(f"\n==== Menu Dashboard ({role.capitalize()}) ====")

        if role.lower() == "admin":
            print("1. Add Initial Menu Items")
            print("2. View Menu")
            print("3. Add New Menu Item")
            print("4. Update Stock")
            print("5. Back")
            choice = input("Enter your choice: ")

            if choice == '1':
                menu_functions["add_initial_items"]()
            elif choice == '2':
                menu_functions["display_menu"]()
            elif choice == '3':
                menu_functions["add_new_item"]()
            elif choice == '4':
                menu_functions["update_stock"]()
            elif choice == '5':
                break
            else:
                print("Invalid choice.")
        else:
            print("1. View Menu")
            print("2. Back")
            choice = input("Enter your choice: ")

            if choice == '1':
                menu_functions["display_menu"]()
            elif choice == '2':
                break
            else:
                print("Invalid choice.")
