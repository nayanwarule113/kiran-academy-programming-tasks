from abc import ABC, abstractmethod
from datetime import datetime


# ============================================================
# KIRAN ACADEMY - TASK 04
# FLIGHT BOOKING CONSOLE APPLICATION USING OOP
# Python 3.x | No external libraries required
# ============================================================


class Passenger(ABC):
    """Abstract base class for all passenger categories."""

    def __init__(self, name: str, age: int):
        self._name = name.strip()
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @abstractmethod
    def get_discount_percentage(self) -> float:
        """Return this passenger category's discount percentage."""
        raise NotImplementedError


class RegularPassenger(Passenger):
    """Regular passengers receive no discount."""

    def get_discount_percentage(self) -> float:
        return 0.0


class StudentPassenger(Passenger):
    """Student passengers receive a 10% discount."""

    def get_discount_percentage(self) -> float:
        return 10.0


class Flight:
    """Stores flight details and controls seat reservations."""

    def __init__(
        self,
        code: str,
        airline: str,
        source: str,
        destination: str,
        available_seats: int,
        base_fare: float,
    ):
        self.__code = code.upper()
        self.__airline = airline
        self.__source = source
        self.__destination = destination
        self.__available_seats = available_seats
        self.__base_fare = base_fare

    @property
    def code(self):
        return self.__code

    @property
    def airline(self):
        return self.__airline

    @property
    def source(self):
        return self.__source

    @property
    def destination(self):
        return self.__destination

    @property
    def available_seats(self):
        return self.__available_seats

    @property
    def base_fare(self):
        return self.__base_fare

    def has_seats(self, count: int) -> bool:
        return 0 < count <= self.__available_seats

    def reserve_seats(self, count: int) -> bool:
        """Change seat count only when the request is valid."""
        if not self.has_seats(count):
            return False
        self.__available_seats -= count
        return True

    def release_seats(self, count: int) -> None:
        """Restore seats if a future feature cancels a booking."""
        if count > 0:
            self.__available_seats += count

    def route(self) -> str:
        return f"{self.__source} to {self.__destination}"

    def display(self) -> None:
        print(
            f"{self.__code:<8} | {self.__airline:<16} | "
            f"{self.route():<25} | {self.__available_seats:>5} | "
            f"Rs. {self.__base_fare:>8,.2f}"
        )


class Booking:
    """Represents one confirmed booking and its fare calculation."""

    def __init__(
        self,
        booking_id: str,
        flight: Flight,
        passenger: Passenger,
        ticket_count: int,
    ):
        self.__booking_id = booking_id
        self.__flight = flight
        self.__passenger = passenger
        self.__ticket_count = ticket_count
        self.__created_at = datetime.now()

        self.__subtotal = flight.base_fare * ticket_count
        self.__discount_percentage = passenger.get_discount_percentage()
        self.__discount_amount = (
            self.__subtotal * self.__discount_percentage / 100
        )
        self.__final_amount = self.__subtotal - self.__discount_amount

    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def flight(self):
        return self.__flight

    @property
    def passenger(self):
        return self.__passenger

    @property
    def ticket_count(self):
        return self.__ticket_count

    @property
    def final_amount(self):
        return self.__final_amount

    @property
    def created_at(self):
        return self.__created_at

    def display_summary(self) -> None:
        passenger_type = (
            "Student"
            if isinstance(self.__passenger, StudentPassenger)
            else "Regular"
        )

        print("\n" + "=" * 48)
        print("               BOOKING SUMMARY")
        print("=" * 48)
        print(f"Booking ID       : {self.__booking_id}")
        print(f"Booking time     : {self.__created_at:%d-%m-%Y %I:%M:%S %p}")
        print(f"Flight code      : {self.__flight.code}")
        print(f"Airline          : {self.__flight.airline}")
        print(f"Route            : {self.__flight.route()}")
        print(f"Passenger        : {self.__passenger.name}")
        print(f"Age              : {self.__passenger.age}")
        print(f"Passenger type   : {passenger_type}")
        print(f"Number of tickets: {self.__ticket_count}")
        print(f"Fare per ticket  : Rs. {self.__flight.base_fare:,.2f}")
        print(f"Subtotal         : Rs. {self.__subtotal:,.2f}")
        print(
            f"Discount ({self.__discount_percentage:g}%)"
            f"   : Rs. {self.__discount_amount:,.2f}"
        )
        print(f"FINAL AMOUNT     : Rs. {self.__final_amount:,.2f}")
        print("=" * 48)


class FlightBookingSystem:
    """Controls the menu, flights, validation, and confirmed bookings."""

    def __init__(self):
        self.__flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Sky India", "Mumbai", "Bengaluru", 30, 3500),
            Flight("PN303", "Air Connect", "Pune", "Hyderabad", 25, 3000),
            Flight("DL404", "Deccan Wings", "Delhi", "Pune", 18, 4200),
        ]
        self.__bookings = []
        self.__next_booking_number = 1001

    def display_flights(self) -> None:
        print("\n" + "=" * 91)
        print("                                  AVAILABLE FLIGHTS")
        print("=" * 91)
        print(
            f"{'Code':<8} | {'Airline':<16} | {'Route':<25} | "
            f"{'Seats':>5} | {'Base fare':>13}"
        )
        print("-" * 91)
        for flight in self.__flights:
            flight.display()
        print("=" * 91)

    def find_flight(self, code: str):
        code = code.strip().upper()
        for flight in self.__flights:
            if flight.code == code:
                return flight
        return None

    @staticmethod
    def validate_booking(flight, name: str, age: int, tickets: int, category: str):
        """Return an error message or None if every field is valid."""
        if flight is None:
            return "Flight code does not exist."
        if not name.strip():
            return "Passenger name cannot be blank."
        if age <= 0:
            return "Age must be greater than zero."
        if tickets <= 0:
            return "Ticket count must be greater than zero."
        if category.lower() not in ("regular", "student"):
            return "Passenger type must be Regular or Student."
        if tickets > flight.available_seats:
            return (
                f"Not enough seats. Requested: {tickets}; "
                f"available: {flight.available_seats}."
            )
        return None

    @staticmethod
    def read_positive_integer(prompt: str):
        """Keep asking until a positive whole number is entered."""
        while True:
            value = input(prompt).strip()
            try:
                number = int(value)
                if number > 0:
                    return number
                print("Please enter a number greater than zero.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    @staticmethod
    def create_passenger(name: str, age: int, category: str) -> Passenger:
        if category.lower() == "student":
            return StudentPassenger(name, age)
        return RegularPassenger(name, age)

    def book_flight(self) -> None:
        print("\n--------------- BOOK A FLIGHT ---------------")
        self.display_flights()

        code = input("Enter flight code: ").strip()
        flight = self.find_flight(code)
        name = input("Enter passenger name: ").strip()
        age = self.read_positive_integer("Enter passenger age: ")

        while True:
            category = input("Passenger type (Regular/Student): ").strip().lower()
            if category in ("regular", "student"):
                break
            print("Please enter either Regular or Student.")

        tickets = self.read_positive_integer("Enter number of tickets: ")

        error = self.validate_booking(flight, name, age, tickets, category)
        if error:
            print(f"\nBOOKING FAILED: {error}")
            print("No booking was created and seat counts were not changed.")
            return

        passenger = self.create_passenger(name, age, category)

        # Prepare the booking first. Do not save it or change seats until
        # all validations have passed.
        booking_id = f"BK{self.__next_booking_number}"
        booking = Booking(booking_id, flight, passenger, tickets)

        # reserve_seats performs its own final availability check.
        if not flight.reserve_seats(tickets):
            print("\nBOOKING FAILED: Not enough seats available.")
            print("No booking was created and seat counts were not changed.")
            return

        self.__bookings.append(booking)
        self.__next_booking_number += 1

        print("\nBOOKING CONFIRMED!")
        booking.display_summary()

    def view_latest_booking(self) -> None:
        if not self.__bookings:
            print("\nNo confirmed booking exists yet. Please book a flight first.")
            return
        self.__bookings[-1].display_summary()

    def run(self) -> None:
        print("\n" + "*" * 48)
        print("          WELCOME TO KIRAN AIR")
        print("           FLIGHT BOOKING SYSTEM")
        print("*" * 48)

        while True:
            print("\nMAIN MENU")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.display_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_latest_booking()
            elif choice == "4":
                print("\nThank you for using Kiran Air. Have a safe journey!")
                break
            else:
                print("Invalid menu choice. Please enter 1, 2, 3, or 4.")


def main():
    application = FlightBookingSystem()
    application.run()


if __name__ == "__main__":
    main()
