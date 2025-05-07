from authentication.admin_login import adminmanager
from authentication.staff_login import staffmanager
from authentication.customer_login import customermanager

def menu():
    while True:
        print("\n======= Restaurant Management System =======")
        print("\n1. for Admin")
        print("2. for Staff")
        print("3. for Customer")
        print("4. for Exit")

        option = input("select your any option:- ")

        if option == '1':
            admin_dashboard()
        elif option == '2':
            staff_dashboard()
        elif option == '3':
            customer_dashboard()
        elif option == '4':
            print("thank you! exiting....")
            break
        else:
            print("invalid option. please try again.")

def admin_dashboard():
    while True:
        print("\n---- Admin Dashboard ----")
        print("\nPress 1 For Register Admin")
        print("Press 2 For View All Admins")
        print("Press 3 For Assign Role to Staff")
        print("Press 4 For Back to Main Menu")

        option = input("please select any option:- ")

        if option == '1':
            adminmanager.register_admin()
        elif option == '2':
            adminmanager.show_all_admins() 
        elif option == '3':
            adminmanager.assign_staff_role()
        elif option == '4':
            break  
        else:
            print("invalid option. please try again.")

def staff_dashboard():
    while True:
        print("\n---- Staff Dashboard ----")
        print("Press 1. For Register Staff")
        print("Press 2. For Staff Login")
        print("Press 3. For View All Staff")
        print("Press 4. For Back to Main Menu")

        option = input("select your any option:- ")

        if option == '1':
            staffmanager.register_staff()
        elif option == '2':
            staffmanager.staff_login()
        elif option == '3':
            staffmanager.list_staff()
        elif option == '4':
            break
        else:
            print("invalid input. please try again.")

def customer_dashboard():
    while True:
        print("\n---- Customer Dashboard ----")
        print("Press 1. For Register Customer")
        print("Press 2. For Customer Login")
        print("Press 3. For View All Customers")
        print("Press 4. For Back to Main Menu")

        option = input("please enter your option:- ")

        if option == '1':
            customermanager.register_customer()
        elif option == '2':
            customermanager.customer_login()
        elif option == '3':
            customermanager.show_customers()
        elif option == '4':
            break
        else:
            print("invalid option. please try again.")
            
menu()
