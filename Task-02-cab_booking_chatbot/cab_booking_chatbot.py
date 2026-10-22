

import random

# ---------- Predefined data ----------
CABS = {
    "1": ("Auto", 12),
    "2": ("Sedan", 18),
    "3": ("SUV", 25),
}

ROUTES = {
    "1": ("Pune Station", "Shivajinagar", 5),
    "2": ("Swargate", "Kothrud", 8),
    "3": ("Hinjawadi", "Wakad", 10),
}

LINE = "=" * 46


def show_main_menu():
    print("\n" + LINE)
    print("        CAB BOOKING CHATBOT")
    print(LINE)
    print("1. Book Ride")
    print("2. Exit")


def choose_cab():
    print("\n--- Choose Cab Type ---")
    for key, (name, rate) in CABS.items():
        print(f"{key}. {name} (Rs. {rate}/km)")
    choice = input("Enter cab choice (1-3): ").strip()
    return CABS.get(choice)  # None if invalid


def choose_route():
    print("\n--- Available Routes ---")
    for key, (src, dest, km) in ROUTES.items():
        print(f"{key}. {src} -> {dest} ({km} km)")
    choice = input("Enter route number (1-3): ").strip()
    return ROUTES.get(choice)  # None if invalid


def generate_otp():
    """Return a random 4-digit OTP (1000-9999)."""
    return random.randint(1000, 9999)


def book_ride():
    cab = choose_cab()
    if cab is None:
        print("Invalid cab choice. Returning to main menu.")
        return
    cab_type, rate = cab

    route = choose_route()
    if route is None:
        print("Invalid route choice. Returning to main menu.")
        return
    source, destination, distance = route

    # Fare = rate per km x distance
    fare = rate * distance

    print("\n" + "-" * 46)
    print("            BOOKING SUMMARY")
    print("-" * 46)
    print(f"Cab Type      : {cab_type}")
    print(f"Source        : {source}")
    print(f"Destination   : {destination}")
    print(f"Distance      : {distance} km")
    print(f"Rate per km   : Rs. {rate}")
    print(f"Total Fare    : Rs. {distance} x {rate} = Rs. {fare}")
    print("-" * 46)

    # Cancellation is possible only BEFORE the OTP is shared
    print("\n1. Confirm & Share OTP")
    print("2. Cancel Ride")
    decision = input("Enter your choice (1-2): ").strip()

    if decision == "1":
        otp = generate_otp()
        print("\n[OK] Booking confirmed!")
        print(f"Your 4-digit OTP is: {otp}")
        print("Share this OTP with the driver to start your ride.")
        print("NOTE: The OTP has been shared, so this ride "
              "can NO LONGER be cancelled.")
    elif decision == "2":
        print("\nRide cancelled successfully. No OTP was shared.")
    else:
        print("Invalid choice. Booking not confirmed. "
              "Returning to main menu.")


def main():
    print("Welcome to the Kiran Cab Booking Chatbot!")
    while True:
        show_main_menu()
        choice = input("Enter your choice (1-2): ").strip()

        if choice == "1":
            book_ride()
        elif choice == "2":
            print("\nThank you for using the Cab Booking Chatbot. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")


if __name__ == "__main__":
    main()
