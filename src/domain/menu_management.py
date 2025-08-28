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

def get_menu_items():
    
    if not os.path.exists(menu_file):
        return []
    
    try:
        with open(menu_file, 'r') as f:
            menu_data = json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

    items = []
    for category, category_items in menu_data.items():
        for item in category_items:
            flat_item = item.copy()
            flat_item["category"] = category
            items.append(flat_item)
    return items

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

    
menu = {}
for category, items in menu.items():
           menu[category] = []
           for item in items:
              item["itemid"] = str(uuid.uuid4())  
              menu[category].append(item)


def save_menu(menu):
 print("Initial menu items added successfully.")

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
            "update_stock": update_stock,
            "get_menu_items": get_menu_items
        }
    else:
        return {
            "display_menu": display_menu,
            "get_menu_items": get_menu_items
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
