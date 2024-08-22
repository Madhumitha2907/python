from db_connector import DatabaseConnector
class Flight:
    def __init__(self, flight_number, destination, departure_time, economy_price, business_price):
        self.flight_number=flight_number
        self.destination=destination
        self.departure_time=departure_time
        self.economy_price=economy_price
        self.business_price=business_price
        
    def save_to_db(self, db_connector):
        query = "INSERT INTO flights (flight_number, destination, departure_time, economy_price, business_price) " \
                "VALUES (%s, %s, %s, %s, %s)"
        values = (self.flight_number, self.destination, self.departure_time, self.economy_price, self.business_price)
        db_connector.execute_query(query, values)
        return f"Flight {self.flight_number} added successfully."
     
    
    
    @staticmethod
    def update_db(db_connector, flight_number, update_data):
        set_clause = ", ".join([f"{col} = %s" for col in update_data.keys()])
        query = f"UPDATE flights SET {set_clause} WHERE flight_number = %s"
        values = list(update_data.values()) + [flight_number]
        db_connector.execute_query(query, values)

    @staticmethod
    def delete_from_db(db_connector, conditions):
        where_clause = " AND ".join([f"{col} = %s" for col in conditions.keys()])
        query = f"DELETE FROM flights WHERE {where_clause}"
        values = list(conditions.values())
        db_connector.execute_query(query, values)

    @staticmethod
    def get_all_from_db(db_connector):
        query = "SELECT * FROM flights"
        return db_connector.fetch_all(query)


