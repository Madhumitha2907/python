from db_connector import DatabaseConnector

class Ticket:
    def __init__(self, reservation_id, seat_number, ticket_type):
        self.reservation_id = reservation_id
        self.seat_number = seat_number
        self.ticket_type = ticket_type

    def save_to_db(self, db_connector):
        query = "INSERT INTO tickets (reservation_id, seat_number, ticket_type) VALUES (%s, %s, %s)"
        values = (self.reservation_id, self.seat_number, self.ticket_type)
        db_connector.execute_query(query, values)


    @staticmethod
    def update_db(db_connector, ticket_id, update_data):
        set_clause = ", ".join([f"{col} = %s" for col in update_data.keys()])
        query = f"UPDATE tickets SET {set_clause} WHERE ticket_id = %s"
        values = list(update_data.values()) + [ticket_id]
        db_connector.execute_query(query, values)

    @staticmethod
    def delete_from_db(db_connector, conditions):
        where_clause = " AND ".join([f"{col} = %s" for col in conditions.keys()])
        query = f"DELETE FROM tickets WHERE {where_clause}"
        values = list(conditions.values())
        db_connector.execute_query(query, values)

    @staticmethod
    def get_all_from_db(db_connector):
        query = "SELECT * FROM tickets"
        return db_connector.fetch_all(query)

