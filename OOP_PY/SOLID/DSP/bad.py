class EmailService:
    def send_email(self, message):
        print("Sending email:", message)


class Notification:
    def __init__(self):
        self.email_service = EmailService()

    def send(self, message):
        self.email_service.send_email(message)


notification = Notification()
notification.send("Hello Akash!")

"""
Why is this bad?
Look at this line: `self.email_service = EmailService()`

The Notification class directly creates and depends on EmailService.
Now, imagine we want to send notifications using SMS instead of email. We would need to modify the Notification class to use SMSService.
The problem: Our main Notification class is tightly connected to a specific service. Changing the service requires changing the main class.
This makes the code harder to extend.
"""