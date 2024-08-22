import getpass
from abc import ABC, abstractmethod

class Flight:
    def __init__(self, flight_number, destination, departure_time, economy_price, business_price):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.economy_price = economy_price
        self.business_price = business_price
    
    def update_details(self, new_destination, new_departure_time, new_economy_price, new_business_price):
        self.destination = new_destination
        self.departure_time = new_departure_time
        self.economy_price = new_economy_price
        self.business_price = new_business_price
    
    def __str__(self):
        return f"Flight {self.flight_number} to {self.destination} at {self.departure_time} (Economy: {self.economy_price}, Business: {self.business_price})"

class Passenger:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
    
    def update_contact_info(self, new_contact_info):
        self.contact_info = new_contact_info
    
    def __str__(self):
        return f"Passenger {self.name}, Contact: {self.contact_info}"

class FrequentFlyer(Passenger):
    def __init__(self, name, contact_info, frequent_flyer_number):
        super().__init__(name, contact_info)
        self.frequent_flyer_number = frequent_flyer_number
    
    def __str__(self):
        return f"Frequent Flyer {self.name}, FF Number: {self.frequent_flyer_number}, Contact: {self.contact_info}"

class StandardPassenger(Passenger):
    pass

class Reservation:
    def __init__(self, passenger, flight):
        self.passenger = passenger
        self.flight = flight
        self.status = "Booked"
    
    def cancel_reservation(self):
        self.status = "Cancelled"
    
    def __str__(self):
        return f"Reservation for {self.passenger.name} on flight {self.flight.flight_number}, Status: {self.status}"

class Ticket(ABC):
    def __init__(self, reservation, seat_number, price):
        self.reservation = reservation
        self.seat_number = seat_number
        self.price = price
    
    @abstractmethod
    def issue_ticket(self):
        pass

class EconomyTicket(Ticket):
    def __init__(self, reservation, seat_number):
        super().__init__(reservation, seat_number, reservation.flight.economy_price)

    def issue_ticket(self):
        return f"Economy Ticket issued for {self.reservation.passenger.name} on flight {self.reservation.flight.flight_number}, Seat {self.seat_number}, Price: {self.price}"

class BusinessTicket(Ticket):
    def __init__(self, reservation, seat_number):
        super().__init__(reservation, seat_number, reservation.flight.business_price)

    def issue_ticket(self):
        return f"Business Ticket issued for {self.reservation.passenger.name} on flight {self.reservation.flight.flight_number}, Seat {self.seat_number}, Price: {self.price}"

class Payment(ABC):
    def __init__(self, balance):
        self.balance = balance
    
    def deduct_amount(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False
    
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        if self.deduct_amount(amount):
            return f"Credit card payment of {amount} processed successfully. Remaining balance: {self.balance}"
        else:
            return "Insufficient balance for credit card payment."

class DebitCardPayment(Payment):
    def process_payment(self, amount):
        if self.deduct_amount(amount):
            return f"Debit card payment of {amount} processed successfully. Remaining balance: {self.balance}"
        else:
            return "Insufficient balance for debit card payment."

class UPIPayment(Payment):
    def process_payment(self, amount):
        if self.deduct_amount(amount):
            return f"UPI payment of {amount} processed successfully. Remaining balance: {self.balance}"
        else:
            return "Insufficient balance for UPI payment."

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AuthenticationSystem:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username, password)

    def authenticate(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return True
        return False

def main():
    auth_system = AuthenticationSystem()
    
    # Registering some users
    try:
        auth_system.register("admin", "admin123")
        auth_system.register("user1", "password1")
    except ValueError as e:
        print(e)

    # Sample data
    flights = [
        Flight("AI101", "New York", "2024-08-01 10:00", 500, 1200),
        Flight("BA202", "London", "2024-08-02 15:00", 400, 1000),
        Flight("AF303", "Paris", "2024-08-03 18:00", 300, 800),
    ]
    
    passengers = [
        FrequentFlyer("Alice", "alice@example.com", "FF12345"),
        StandardPassenger("Bob", "bob@example.com")
    ]
    
    reservations = []
    tickets = []
    
    # Authentication
    print("Please login to access the Flight Booking System")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    
    if not auth_system.authenticate(username, password):
        print("Authentication failed! Exiting...")
        return

    while True:
        print("\n--- Flight Booking System ---")
        print("1. View Flights")
        print("2. Add Reservation")
        print("3. View Reservations")
        print("4. Issue Ticket")
        print("5. Process Payment")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("\n--- Available Flights ---")
            for flight in flights:
                print(flight)
        
        elif choice == "2":
            print("\n--- Add Reservation ---")
            try:
                passenger_name = input("Enter passenger name: ")
                passenger = next((p for p in passengers if p.name == passenger_name), None)
                
                if not passenger:
                    raise ValueError("Passenger not found!")
                
                flight_number = input("Enter flight number: ")
                flight = next((f for f in flights if f.flight_number == flight_number), None)
                
                if not flight:
                    raise ValueError("Flight not found!")
                
                reservation = Reservation(passenger, flight)
                reservations.append(reservation)
                print("Reservation added!")
            except ValueError as e:
                print(e)
        
        elif choice == "3":
            print("\n--- Reservations ---")
            if not reservations:
                print("No reservations found.")
            for i, reservation in enumerate(reservations):
                print(f"{i}. {reservation}")
        
        elif choice == "4":
            print("\n--- Issue Ticket ---")
            try:
                reservation_id = int(input("Enter reservation ID (index): "))
                
                if reservation_id >= len(reservations) or reservation_id < 0:
                    raise ValueError("Invalid reservation ID!")
                
                reservation = reservations[reservation_id]
                seat_number = input("Enter seat number: ")
                ticket_type = input("Enter ticket type (economy/business): ").lower()
                
                if ticket_type == "economy":
                    ticket = EconomyTicket(reservation, seat_number)
                elif ticket_type == "business":
                    ticket = BusinessTicket(reservation, seat_number)
                else:
                    raise ValueError("Invalid ticket type!")
                
                tickets.append(ticket)
                print(ticket.issue_ticket())
            except ValueError as e:
                print(e)
        
        elif choice == "5":
            print("\n--- Process Payment ---")
            try:
                ticket_id = int(input("Enter ticket ID (index): "))
                
                if ticket_id >= len(tickets) or ticket_id < 0:
                    raise ValueError("Invalid ticket ID!")
                
                ticket = tickets[ticket_id]
                amount = ticket.price
                payment_method = input("Enter payment method (credit/debit/upi): ").lower()
                balance = float(input("Enter your balance: "))
                
                if payment_method == "credit":
                    payment = CreditCardPayment(balance)
                elif payment_method == "debit":
                    payment = DebitCardPayment(balance)
                elif payment_method == "upi":
                    payment = UPIPayment(balance)
                else:
                    raise ValueError("Invalid payment method!")
                
                print(payment.process_payment(amount))
            except ValueError as e:
                print(e)
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
