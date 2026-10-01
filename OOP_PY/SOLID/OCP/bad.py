class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # Responsibility 1: User data
    def display_user(self):
        print(self.name, self.email)

    # Responsibility 2: Database operations
    def save_to_database(self):
        print("Saving user to database...")

    # Responsibility 3: Email operations
    def send_email(self):
        print("Sending email to", self.email)


user = User("Akash", "akash@gmail.com")

user.display_user()
user.save_to_database()
user.send_email()

"""
Now, imagine the database changes from MySQL to MongoDB. You need to modify the User class to update the database code.
Similarly, if the email system changes, you need to modify the same User class again.
The problem: The User class should only manage user information, but it is also handling database and email work.
"""