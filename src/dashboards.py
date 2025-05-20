from authentication.admin_login import admin_auth_menu
from authentication.staff_login import staff_auth_menu
from authentication.customer_login import customer_auth_menu
from domain.menu_management import (
    add_initial_menu_items,
    menu_management,
    menu_management_dashboard
)
from domain.order_processing import order_processing_dashboard
from domain.generating_bills import generate_bill
from domain.table_booking import book_table, view_all_bookings  

def admin_menu_dashboard():
    menu = menu_management('admin')  

    while True:
        print("\n--- Menu Management (Admin) ---")
        print("1. Add Menu Item")
        print("2. Update Menu Item")
        print("3. Delete Menu Item")
        print("4. View All Items")
        print("5. Back")

        choice = input("Select an option: ")

        if choice == '1':
            menu.add_item()
        elif choice == '2':
            menu.update_item()
        elif choice == '3':
            menu.delete_item()
        elif choice == '4':
            menu_management_dashboard('admin', menu)
        elif choice == '5':
            break
        else:
            print("Invalid option!")


def admin_dashboard():
    print("\n--- Admin Dashboard ---")
    while True:
        print("\n1. Menu Management")
        print("2. Order Processing")
        print("3. Table Booking")             
        print("4. View All Booked Tables")    
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")
        if choice == '1':
            admin_menu_dashboard()
        elif choice == '2':
            order_processing_dashboard()
        elif choice == '3':
            book_table()
        elif choice == '4':
            view_all_bookings()
        elif choice == '5':
            break
        else:
            print("Invalid option.")


def staff_dashboard():
    print("\n--- Staff Dashboard ---")
    menu = menu_management('staff')  

    while True:
        print("\n1. View Menu")
        print("2. Order Processing")
        print("3. Table Booking")           
        print("4. View All Booked Tables") 
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")
        if choice == '1':
            menu_management_dashboard('staff', menu)
        elif choice == '2':
            order_processing_dashboard()
        elif choice == '3':
            book_table()
        elif choice == '4':
            view_all_bookings()
        elif choice == '5':
            break
        else:
            print("Invalid option.")


def customer_dashboard(customer_id):
    print(f"\n--- Customer Dashboard (ID: {customer_id}) ---")
    menu = menu_management('customer') 
    while True:
        print("\n1. View Menu")
        print("2. Place Order")
        print("3. Generate Bill")
        print("4. Book a Table")             
        print("5. View Booked Tables")      
        print("6. Back to Main Menu")

        choice = input("Enter choice: ")
        if choice == '1':
            menu_management_dashboard('customer', menu)
        elif choice == '2':
            order_processing_dashboard(customer_id)
        elif choice == '3':
            generate_bill(customer_id)
        elif choice == '4':
            book_table()
        elif choice == '5':
            view_all_bookings()
        elif choice == '6':
            break
        else:
            print("Invalid option.")


def menu_dashboards():
    add_initial_menu_items()

    while True:
        print("\n====== Welcome to Restaurant Management System ======")
        print("1. Admin Login")
        print("2. Staff Login")
        print("3. Customer Login")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            role = admin_auth_menu()
            if role == 'admin':
                admin_dashboard()

        elif choice == '2':
            role = staff_auth_menu()
            if role == 'staff':
                staff_dashboard()

        elif choice == '3':
            customer_id = customer_auth_menu()
            if customer_id:
                customer_dashboard(customer_id)

        elif choice == '4':
            print("Exiting system. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu_dashboards()
