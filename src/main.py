from authentication.admin_login import admin_signup, admin_login
from authentication.customer_login import customer_signup, customer_login
from authentication.staff_login import staff_signup, staff_login

def main():
    while True:
        print("\n=== Restaurant Management System ===")
        print("Press 1. For Admin Sign Up")
        print("Press 2. For Admin Login")
        print("Press 3. For Customer Sign Up")
        print("Press 4. For Customer Login")
        print("Press 5. For Staff Sign Up")
        print("Press 6. For Staff Login")
        print("Press 7. For Exiting\n")

        Option = input("Please enter your any option:- ")

        if Option == "1":
            admin_signup()
        elif Option == "2":
            admin_login()
        elif Option == "3":
            customer_signup()
        elif Option == "4":
            customer_login()
        elif Option == "5":
            staff_signup()
        elif Option == "6":
            staff_login()
        elif Option == "7":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

main()
