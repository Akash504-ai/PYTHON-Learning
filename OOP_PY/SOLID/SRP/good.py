class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_user(self):
        print(self.name, self.email)


class UserRepository:
    def save_to_database(self, user):
        print("Saving user to database...")


class EmailService:
    def send_email(self, user):
        print("Sending email to", user.email)


# Creating objects
user = User("Akash", "akash@gmail.com")

repository = UserRepository()
email_service = EmailService()

user.display_user()
repository.save_to_database(user)
email_service.send_email(user)


# Each class has a distinct responsibility. If the email implementation changes, you can modify EmailService without changing User.
