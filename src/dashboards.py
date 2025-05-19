# # 
# from authentication.admin_login import admin_auth_menu
# from authentication.staff_login import staff_login
# from authentication.customer_login import customer_auth_menu
# from domain.menu_management import menu_management, menu_management_dashboard
# from domain.order_processing import order_processing_dashboard
# from domain.table_booking import table_booking_dashboard
# from domain.generating_bills import generate_bill
# from manage_error.exceptions_handler import handle_exception
# from log.logger import log_event

# def admin_dashboard():
#     try:
#         admin_auth_menu()
#     except Exception as e:
#         handle_exception("admin_dashboard", e)

# def staff_dashboard():
#     try:
#         role = staff_login()
#         if role == "staff":
#             role_key = "staff"
#             funcs = menu_management(role_key)
#             while True:
#                 print("\n--- Staff Dashboard ---")
#                 print("1. View Menu")
#                 print("2. Order Processing")
#                 print("3. Table Booking")
#                 print("4. Logout")

#                 choice = input("Enter your choice: ")
#                 if choice == '1':
#                     menu_management_dashboard(role_key, funcs)
#                 elif choice == '2':
#                     order_processing_dashboard()
#                 elif choice == '3':
#                     table_booking_dashboard()
#                 elif choice == '4':
#                     print("Logging out from staff panel...\n")
#                     break
#                 else:
#                     print("Invalid choice, please try again.")
#     except Exception as e:
#         handle_exception("staff_dashboard", e)

# def customer_dashboard():
#     try:
#         result = customer_auth_menu()
#         if result == "customer":
#             from authentication.customer_login import get_last_customer_id
#             customer_id = get_last_customer_id()

#             role_key = "customer"
#             funcs = menu_management(role_key)
#             while True:
#                 print("\n--- Customer Dashboard ---")
#                 print("1. View Menu")
#                 print("2. Place Order")
#                 print("3. Book Table")
#                 print("4. Generate Bill")
#                 print("5. Logout")

#                 choice = input("Enter your choice: ")
#                 if choice == '1':
#                     menu_management_dashboard(role_key, funcs)
#                 elif choice == '2':
#                     order_processing_dashboard(customer_id)
#                 elif choice == '3':
#                     table_booking_dashboard()
#                 elif choice == '4':
#                     generate_bill(customer_id)
#                 elif choice == '5':
#                     print("Logging out from customer dashboard...\n")
#                     break
#                 else:
#                     print("Invalid choice, please try again.")
#     except Exception as e:
#         handle_exception("customer_dashboard", e)

# def main_dashboard():
#     while True:
#         print("\n======= Restaurant Management System =======")
#         print("1. Admin dashboard")
#         print("2. Staff dashboard")
#         print("3. Customer dashboard")
#         print("4. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             admin_dashboard()
#         elif choice == '2':
#             staff_dashboard()
#         elif choice == '3':
#             customer_dashboard()
#         elif choice == '4':
#             print("Exiting... Thank you!")
#             break
#         else:
#             print("Invalid choice, please try again.")

# if __name__ == "__main__":
#     log_event("info", "Application started")
#     try:
#         main_dashboard()
#     except Exception as e:
#         handle_exception("main_dashboard", e)
#     finally:
#         log_event("info", "Application exited")
# dashboard.py

from authentication.admin_login import admin_auth_menu
from authentication.staff_login import staff_auth_menu
from authentication.customer_login import customer_auth_menu
from domain.menu_management import (
    add_initial_menu_items,
    menu_management,
    menu_management_dashboard
)

def menu_dashboards():
  
    add_initial_menu_items()

    while True:
        print("\n=== Restaurant Management System ===")
        print("1. Admin Dashboard")
        print("2. Staff Dashboard")
        print("3. Customer Dashboard")
        print("4. View Menu (Guest)")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            # Admin logs in and accesses full menu management
            role = admin_auth_menu()
            if role == 'admin':
                menu_funcs = menu_management(role)
                menu_management_dashboard(role, menu_funcs)

        elif choice == '2':
            role = staff_auth_menu()
            if role:
                # Staff can only view the menu
                menu_funcs = menu_management('staff')
                menu_management_dashboard('staff', menu_funcs)

        elif choice == '3':
            role = customer_auth_menu()
            if role:
                # Customer can only view the menu
                menu_funcs = menu_management('customer')
                menu_management_dashboard('customer', menu_funcs)

        elif choice == '4':
            # Guests (no login) can only view menu
            menu_funcs = menu_management('guest')
            menu_management_dashboard('guest', menu_funcs)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu_dashboards()
