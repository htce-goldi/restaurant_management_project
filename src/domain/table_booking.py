import json
import os
import uuid

# टेबल की कुल सीट्स (यहाँ आप अपनी रेस्टोरेंट के अनुसार बदल सकते हैं)
table_capacity = {
    "T1": 4,
    "T2": 6,
    "T3": 2,
    "T4": 8
}

def is_valid_name(name):
    return name.replace(" ", "").isalpha()

def is_valid_mobile(mobile):
    return mobile.isdigit() and len(mobile) == 10

def is_table_available(table_number):
    if not os.path.exists("database/table_bookings.json"):
        return True
    with open("database/table_bookings.json", "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
    for booking in data:
        if booking["table_number"] == table_number:
            return False
    return True

def book_table():
    print("\n--- Table Booking ---")
    name = input("Enter your name: ")
    while not is_valid_name(name):
        print("Invalid name! Only letters and spaces allowed.")
        name = input("Enter your name: ")

    mobile = input("Enter your 10-digit mobile number: ")
    while not is_valid_mobile(mobile):
        print("Invalid mobile number! Enter only 10 digits.")
        mobile = input("Enter your 10-digit mobile number: ")

    table_number = input("Enter table number to book (e.g., T1, T2, T3): ").upper()
    while table_number not in table_capacity:
        print("Invalid table number! Available tables:", ", ".join(table_capacity.keys()))
        table_number = input("Enter table number to book: ").upper()

    if not is_table_available(table_number):
        print(f"Table {table_number} is already booked. Please choose another table.")
        return

    booking_time = input("Enter booking time (e.g., 7:30 PM): ")

    booking_data = {
        "booking_id": str(uuid.uuid4()),
        "name": name,
        "mobile": mobile,
        "table_number": table_number,
        "booking_time": booking_time
    }

    if not os.path.exists("database/table_bookings.json"):
        with open("database/table_bookings.json", "w") as file:
            json.dump([booking_data], file, indent=4)
    else:
        with open("database/table_bookings.json", "r+") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
            data.append(booking_data)
            file.seek(0)
            json.dump(data, file, indent=4)

    print(f"\nTable {table_number} successfully booked for {name} at {booking_time}.")

def view_all_bookings():
    print("\n--- All Table Bookings ---")
    if not os.path.exists("database/table_bookings.json"):
        print("No bookings available.")
        return

    with open("database/table_bookings.json", "r") as file:
        try:
            data = json.load(file)
            if not data:
                print("No bookings found.")
                return
        except json.JSONDecodeError:
            print("Error reading booking data.")
            return

    for booking in data:
        print(f"\nBooking ID: {booking['booking_id']}")
        print(f"Name: {booking['name']}")
        print(f"Mobile: {booking['mobile']}")
        print(f"Table Number: {booking['table_number']}")
        print(f"Booking Time: {booking['booking_time']}")

def view_table_status():
    print("\n--- Table Status ---")

    # पहले सभी बुकिंग्स लोड करें
    if not os.path.exists("database/table_bookings.json"):
        bookings = []
    else:
        with open("database/table_bookings.json", "r") as file:
            try:
                bookings = json.load(file)
            except json.JSONDecodeError:
                bookings = []

 
    booked_counts = {table: 0 for table in table_capacity.keys()}
    for booking in bookings:
        tbl = booking.get("table_number")
        if tbl in booked_counts:
            booked_counts[tbl] += 1

    for table, capacity in table_capacity.items():
        booked = booked_counts.get(table, 0)
        available = capacity - booked
        print(f"{table} | Total: {capacity} | Booked: {booked} | Available: {available}")

if __name__ == "__main__":
    while True:
        print("\n1. Book a Table")
        print("2. View All Bookings")
        print("3. View Table Status")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            book_table()
        elif choice == '2':
            view_all_bookings()
        elif choice == '3':
            view_table_status()
        elif choice == '4':
            break
        else:
            print("Invalid choice, try again.")
