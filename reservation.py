from db_connector import DatabaseConnector

class Reservation:
    def __init__(self, passenger_id, flight_number, status="Booked"):
        self.passenger_id = passenger_id
        self.flight_number = flight_number
        self.status = status

    def save_to_db(self, db_connector):
        query = "INSERT INTO reservations (passenger_id, flight_number, status) VALUES (%s, %s, %s)"
        values = (self.passenger_id, self.flight_number, self.status)
        db_connector.execute_query(query, values)

    @staticmethod
    def update_db(db_connector, reservation_id, update_data):
        set_clause = ", ".join([f"{col} = %s" for col in update_data.keys()])
        query = f"UPDATE reservations SET {set_clause} WHERE reservation_id = %s"
        values = list(update_data.values()) + [reservation_id]
        db_connector.execute_query(query, values)

    @staticmethod
    def delete_from_db(db_connector, conditions):
        where_clause = " AND ".join([f"{col} = %s" for col in conditions.keys()])
        query = f"DELETE FROM reservations WHERE {where_clause}"
        values = list(conditions.values())
        db_connector.execute_query(query, values)

    @staticmethod
    def get_all_from_db(db_connector):
        query = "SELECT * FROM reservations"
        return db_connector.fetch_all(query)
