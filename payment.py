from db_connector import DatabaseConnector

class Payment:
    def __init__(self, reservation_id, amount, payment_method):
        self.reservation_id = reservation_id
        self.amount = amount
        self.payment_method = payment_method

    def save_to_db(self, db_connector):
        query = "INSERT INTO payments (reservation_id, amount, payment_method) VALUES (%s, %s, %s)"
        values = (self.reservation_id, self.amount, self.payment_method)
        db_connector.execute_query(query, values)

    @staticmethod
    def update_db(db_connector, payment_id, update_data):
        set_clause = ", ".join([f"{col} = %s" for col in update_data.keys()])
        query = f"UPDATE payments SET {set_clause} WHERE payment_id = %s"
        values = list(update_data.values()) + [payment_id]
        db_connector.execute_query(query, values)

    @staticmethod
    def delete_from_db(db_connector, conditions):
        where_clause = " AND ".join([f"{col} = %s" for col in conditions.keys()])
        query = f"DELETE FROM payments WHERE {where_clause}"
        values = list(conditions.values())
        db_connector.execute_query(query, values)

    @staticmethod
    def get_all_from_db(db_connector):
        query = "SELECT * FROM payments"
        return db_connector.fetch_all(query)


    