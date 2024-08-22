import getpass

# Authenticator Class
class Authenticator:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            raise ValueError("User already exists!")
        self.users[username] = password

    def authenticate(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        return False

# Main Function
def main():
    authenticator = Authenticator()

    # Registering some users
    try:
        authenticator.register("admin", "admin123")
        authenticator.register("user1", "password1")
    except ValueError as e:
        print(e)

    # Authentication
    print("Please login to access the Flight Booking System")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if not authenticator.authenticate(username, password):
        print("Authentication failed! Exiting...")
        return
    else:
        print("Welcome")    

    # Proceed with your flight booking system logic here
    # This part would include interacting with flights, reservations, tickets, etc.

if __name__ == "__main__":
    main()
