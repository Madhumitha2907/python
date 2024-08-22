from db_connector import DatabaseConnector
from flight import Flight
from passenger import Passenger
from reservation import Reservation
from ticket import Ticket
from payment import Payment
from getpass import getpass

def main():
    db_connector = DatabaseConnector('localhost', 'root', 'root123', 'flight_booking_system')
    db_connector.connect()

    try:
        
        db_connector.execute_query("CREATE TABLE IF NOT EXISTS flights (flight_number VARCHAR(10) PRIMARY KEY, destination VARCHAR(100), departure_time DATETIME, economy_price DECIMAL(10, 2), business_price DECIMAL(10, 2))")
        db_connector.execute_query("CREATE TABLE IF NOT EXISTS passengers (passenger_name VARCHAR(100) PRIMARY KEY, contact_info VARCHAR(255))")
        db_connector.execute_query("CREATE TABLE IF NOT EXISTS reservations (id INT AUTO_INCREMENT PRIMARY KEY, passenger_name VARCHAR(100), flight_number VARCHAR(10), status VARCHAR(50), FOREIGN KEY (passenger_name) REFERENCES passengers(name), FOREIGN KEY (flight_number) REFERENCES flights(flight_number))")
        db_connector.execute_query("CREATE TABLE IF NOT EXISTS tickets (id INT AUTO_INCREMENT PRIMARY KEY, reservation_id INT, seat_number VARCHAR(10), ticket_type ENUM('Economy', 'Business'), FOREIGN KEY (reservation_id) REFERENCES reservations(id))")
        db_connector.execute_query("CREATE TABLE IF NOT EXISTS payments (id INT AUTO_INCREMENT PRIMARY KEY, reservation_id INT, amount DECIMAL(10, 2), payment_method ENUM('Credit Card', 'Debit Card', 'UPI'), FOREIGN KEY (reservation_id) REFERENCES reservations(id))")
        
        while True:
            print("\n--- Flight Booking System ---")
            print("1. Add Flight")
            print("2. Add Passenger")
            print("3. Add Reservation")
            print("4. Ticket")
            print("5. Payment")
            print("6. Details")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("\n--- Add Flight ---")
                flight_number = input("Enter flight number: ")
                destination = input("Enter destination: ")
                departure_time = input("Enter departure time (YYYY-MM-DD HH:MM): ")
                economy_price = float(input("Enter economy price: "))
                business_price = float(input("Enter business price: "))

                flight = Flight(flight_number, destination, departure_time, economy_price, business_price)
                flight.save_to_db(db_connector)
                print("Flight added successfully.")

            elif choice == "2":
                print("\n--- Add Passenger ---")
                name = input("Enter passenger name: ")
                contact_info = input("Enter contact info: ")

                passenger = Passenger(name, contact_info)
                passenger.save_to_db(db_connector)
                print("Passenger added successfully.")

            elif choice == "3":
                print("\n--- Add Reservation ---")
                passenger_id = input("Enter passenger id: ")
                flight_number = input("Enter flight number: ")
                status = "Booked"

                reservation = Reservation(passenger_id, flight_number, status)
                reservation.save_to_db(db_connector)
                print("Reservation added successfully.")

            elif choice == "4":
                print("\n--- Add Ticket ---")
                reservation_id = input("Enter reservation ID: ")
                seat_number = input("Enter seat number: ")
                ticket_type = input("Enter ticket type (Economy/Business): ")

                ticket = Ticket(reservation_id, seat_number, ticket_type)
                ticket.save_to_db(db_connector)
                print("Ticket added successfully.")

            elif choice == "5":
                print("\n--- Add Payment ---")
                reservation_id = input("Enter reservation ID: ")
                amount = float(input("Enter payment amount: "))
                payment_method = input("Enter payment method (Credit Card/Debit Card/UPI): ")

                payment = Payment(reservation_id, amount, payment_method)
                payment.save_to_db(db_connector)
                print("Payment added successfully.")
            elif choice=="7":
                table_name = input("Enter the table name :")
                column_name = input("Enter the column_name where to update:")
                new_value = input("Enter the new_value :")
                condition_column = input("Enter the condition_column :")
                condition_value = input("Enter the condition_value :")
                updated_records = db_connector.update_single_column(table_name, column_name, new_value, condition_column, condition_value)
                print("Updated records:", updated_records)
                
                break
            elif choice == "6":
                print("\n--- View Details ---")
                view_choice = input("What details do you want to view?\n"
                                    "1. Flights\n"
                                    "2. Passengers\n"
                                    "3. Reservations\n"
                                    "4. Tickets\n"
                                    "5. Payments\n"
                                    "Enter your choice: ")

                if view_choice == "1":
                    print("\n--- Flights ---")
                    try:
                        flights = Flight.get_all_flights(db_connector)
                        for flight in flights:
                            print(flight)
                    except Exception as e:
                        print(f"Error: {e}")


                elif view_choice == "2":
                    print("\n--- Passengers ---")
                    try:
                        passengers =Passenger.get_all_passengers(db_connector)
                        for passenger in passengers:
                            print(passenger)
                    except Exception as e:
                        print(f"Error: {e}")

                elif view_choice == "3":
                    print("\n--- Reservations ---")
                    try:
                        reservations = Reservation.get_all_reservations(db_connector)
                        for reservation in reservations:
                            print(reservation)
                    except Exception as e:
                        print(f"Error: {e}")


                elif view_choice == "4":
                    print("\n--- Tickets ---")
                    try:
                        tickets = Ticket.get_all_tickets(db_connector)
                        for ticket in tickets:
                            print(ticket)
                    except Exception as e:
                        print(f"Error: {e}")

                elif view_choice == "5":
                    print("\n--- Payments ---")
                    try:
                        payments = Payment.get_all_payments(db_connector)
                        for payment in payments:
                            print(payment)
                    except Exception as e:
                        print(f"Error: {e}")

                else:
                    print("Invalid choice. Please try again.")

            else:
                print("Invalid choice. Please try again.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        db_connector.close_connection()

if __name__ == "__main__":
    main()
