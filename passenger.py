from db_connector import DatabaseConnector

class Passenger:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def save_to_db(self, db_connector):
        query = "INSERT INTO passengers (passenger_name, contact_info) VALUES (%s, %s)"
        values = (self.name, self.contact_info)
        db_connector.execute_query(query, values)

  
    @staticmethod
    def get_all_from_db(db_connector):
        query = "SELECT * FROM passengers"
        cursor = db_connector.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    @staticmethod
    def update_db(db_connector, passenger_id, update_data):
        set_clause = ", ".join([f"{col} = %s" for col in update_data.keys()])
        query = f"UPDATE passengers SET {set_clause} WHERE passenger_id = %s"
        values = list(update_data.values()) + [passenger_id]
        db_connector.execute_query(query, values)

    @staticmethod
    def delete_from_db(db_connector, conditions):
        where_clause = " AND ".join([f"{col} = %s" for col in conditions.keys()])
        query = f"DELETE FROM passengers WHERE {where_clause}"
        values = list(conditions.values())
        db_connector.execute_query(query, values)
    