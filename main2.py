# main.py

from db_connector import DatabaseConnector
from flight import Flight
from passenger import Passenger
from reservation import Reservation
from ticket import Ticket
from payment import Payment

def get_user_input(prompt):
    return input(prompt).strip()

def get_update_conditions():
    conditions = {}
    print("Enter details to update:")
    while True:
        column = get_user_input("Column name (or type 'done' to finish): ")
        if column.lower() == 'done':
            break
        value = get_user_input(f"New value for {column}: ")
        conditions[column] = value
    return conditions

def get_delete_conditions():
    conditions = {}
    print("Enter details to delete:")
    while True:
        column = get_user_input("Column name (or type 'done' to finish): ")
        if column.lower() == 'done':
            break
        value = get_user_input(f"Value for {column}: ")
        conditions[column] = value
    return conditions
def get_reservations_with_flight_and_passenger(db_connector):
    query = """
    SELECT r.reservation_id, r.status, f.flight_number, f.destination, f.departure_time, p.passenger_name, p.contact_info
    FROM reservations r
    INNER JOIN flights f ON r.flight_number = f.flight_number
    INNER JOIN passengers p ON r.passenger_id = p.passenger_id;
    """
    results = db_connector.fetch_all(query)
    for row in results:
        print(row)

def get_flights_with_reservations(db_connector):
    query = """
    SELECT f.flight_number, f.destination, f.departure_time, r.reservation_id, r.status
    FROM flights f
    LEFT JOIN reservations r ON f.flight_number = r.flight_number;
    """
    results = db_connector.fetch_all(query)
    for row in results:
        print(row)

def get_reservations_with_flights(db_connector):
    query = """
    SELECT r.reservation_id, r.status, f.flight_number, f.destination, f.departure_time
    FROM reservations r
    RIGHT JOIN flights f ON r.flight_number = f.flight_number;
    """
    results = db_connector.fetch_all(query)
    for row in results:
        print(row)



def main():
    db_connector = DatabaseConnector(host="localhost", user="root", password="root123", database="flight_booking_system")
    db_connector.connect()

    while True:
        print("\n--- Flight Booking System ---")
        print("1. Add Flight")
        print("2. Add Passenger")
        print("3. Add Reservation")
        print("4. Add Ticket")
        print("5. Add Payment")
        print("6. Update Record")
        print("7. Delete Record")
        print("8. View All Flights")
        print("9. View All Passengers")
        print("10. View All Reservations")
        print("11. View All Tickets")
        print("12. View All Payments")
        print("13. View Reservations with Flight and Passenger")
        print("14. View Flights with Reservations")
        print("15. View Reservations with Flights")
        #print("16. View All Flights and Reservations")
        print("16. Exit")

        choice = get_user_input("Enter your choice: ")

        if choice == "1":
            # Add Flight logic
            flight_number = get_user_input("Enter flight number: ")
            destination = get_user_input("Enter destination: ")
            departure_time = get_user_input("Enter departure time (YYYY-MM-DD HH:MM): ")
            economy_price = float(get_user_input("Enter economy price: "))
            business_price = float(get_user_input("Enter business price: "))
            flight = Flight(flight_number, destination, departure_time, economy_price, business_price)
            flight.save_to_db(db_connector)
            print("Flight added successfully.")

        elif choice == "2":
            # Add Passenger logic
            name = get_user_input("Enter passenger name: ")
            contact_info = get_user_input("Enter contact info: ")
            passenger = Passenger(name, contact_info)
            passenger.save_to_db(db_connector)
            print("Passenger added successfully.")

        elif choice == "3":
            # Add Reservation logic
            passenger_id = get_user_input("Enter passenger id: ")
            flight_number = get_user_input("Enter flight number: ")
            status = "Booked"
            reservation = Reservation(passenger_id, flight_number, status)
            reservation.save_to_db(db_connector)
            print("Reservation added successfully.")

        elif choice == "4":
            # Add Ticket logic
            reservation_id = int(get_user_input("Enter reservation ID: "))
            seat_number = get_user_input("Enter seat number: ")
            ticket_type = get_user_input("Enter ticket type (Economy/Business): ")
            #price = float(get_user_input("Enter ticket price: "))
            ticket = Ticket(reservation_id, seat_number, ticket_type)
            ticket.save_to_db(db_connector)
            print("Ticket added successfully.")

        elif choice == "5":
            # Add Payment logic
            reservation_id = int(get_user_input("Enter reservation ID: "))
            amount = float(get_user_input("Enter amount: "))
            payment_method = get_user_input("Enter payment method (Credit Card/Debit Card/UPI): ")
            payment = Payment(reservation_id, amount, payment_method)
            payment.save_to_db(db_connector)
            print("Payment added successfully.")

        elif choice == "6":
            # Update Record logic
            print("Choose table to update:")
            print("1. Flight")
            print("2. Passenger")
            print("3. Reservation")
            print("4. Ticket")
            print("5. Payment")
            table_choice = get_user_input("Enter your choice: ")

            if table_choice == "1":
                flight_number = get_user_input("Enter the flight number to update: ")
                conditions = get_update_conditions()
                Flight.update_db(db_connector, flight_number, conditions)
                print("Flight updated successfully.")

            elif table_choice == "2":
                passenger_id = int(get_user_input("Enter the passenger ID to update: "))
                conditions = get_update_conditions()
                Passenger.update_db(db_connector, passenger_id, conditions)
                print("Passenger updated successfully.")

            elif table_choice == "3":
                reservation_id = int(get_user_input("Enter the reservation ID to update: "))
                conditions = get_update_conditions()
                Reservation.update_db(db_connector, reservation_id, conditions)
                print("Reservation updated successfully.")

            elif table_choice == "4":
                ticket_id = int(get_user_input("Enter the ticket ID to update: "))
                conditions = get_update_conditions()
                Ticket.update_db(db_connector, ticket_id, conditions)
                print("Ticket updated successfully.")

            elif table_choice == "5":
                payment_id = int(get_user_input("Enter the payment ID to update: "))
                conditions = get_update_conditions()
                Payment.update_db(db_connector, payment_id, conditions)
                print("Payment updated successfully.")

        elif choice == "7":
            # Delete Record logic
            print("Choose table to delete from:")
            print("1. Flight")
            print("2. Passenger")
            print("3. Reservation")
            print("4. Ticket")
            print("5. Payment")
            table_choice = get_user_input("Enter your choice: ")

            if table_choice == "1":
                conditions = get_delete_conditions()
                Flight.delete_from_db(db_connector, conditions)
                print("Flight deleted successfully.")

            elif table_choice == "2":
                conditions = get_delete_conditions()
                Passenger.delete_from_db(db_connector, conditions)
                print("Passenger deleted successfully.")

            elif table_choice == "3":
                conditions = get_delete_conditions()
                Reservation.delete_from_db(db_connector, conditions)
                print("Reservation deleted successfully.")

            elif table_choice == "4":
                conditions = get_delete_conditions()
                Ticket.delete_from_db(db_connector, conditions)
                print("Ticket deleted successfully.")

            elif table_choice == "5":
                conditions = get_delete_conditions()
                Payment.delete_from_db(db_connector, conditions)
                print("Payment deleted successfully.")

        elif choice == "8":
            flights = Flight.get_all_from_db(db_connector)
            print("All Flights:")
            for flight in flights:
                print(flight)

        elif choice == "9":
            passengers = Passenger.get_all_from_db(db_connector)
            print("All Passengers:")
            for passenger in passengers:
                print(passenger)

        elif choice == "10":
            reservations = Reservation.get_all_from_db(db_connector)
            print("All Reservations:")
            for reservation in reservations:
                print(reservation)

        elif choice == "11":
            tickets = Ticket.get_all_from_db(db_connector)
            print("All Tickets:")
            for ticket in tickets:
                print(ticket)
        elif choice == "12":
            payments = Payment.get_all_from_db(db_connector)
            print("All Payments:")
            for payment in payments:
                print(payment)
        elif choice == "13":

            get_reservations_with_flight_and_passenger(db_connector)

        elif choice == "14":
            get_flights_with_reservations(db_connector)

        elif choice == "15":
            get_reservations_with_flights(db_connector)
        
        elif choice == "16":
            print("Exiting Flight Booking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    db_connector.close_connection()

if __name__ == "__main__":
    main()
