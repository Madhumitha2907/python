import pymysql
from authenticator import Authenticator

def main():
    # Example usage of Authenticator
    auth = Authenticator("admin", "ecret")
    if auth.authenticate():
        print("Authentication successful")
    else:
        print("Authentication failed")

if __name__ == "__main__":
    main()
connection=pymysql.connect(host="localhost",user="root",passwd="root123",database="flightbookingsystem")
cursor=connection.cursor()
query="select * from passengers"
cursor.execute(query)
rows=cursor.fetchall()
for row in rows:
    print(row)
main()
connection.commit()
connection.close()    