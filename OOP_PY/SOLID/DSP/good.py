class NotificationService:
    def send(self, message):
        pass


class EmailService(NotificationService):
    def send(self, message):
        print("Sending email:", message)


class SMSService(NotificationService):
    def send(self, message):
        print("Sending SMS:", message)


class Notification:
    def __init__(self, service):
        self.service = service

    def send(self, message):
        self.service.send(message)


# Using email
email = EmailService()
notification1 = Notification(email)
notification1.send("Hello Akash!")

# Using SMS
sms = SMSService()
notification2 = Notification(sms)
notification2.send("Hello Akash!")


"""
Why is this good?
Notice this line:
def __init__(self, service):    
    self.service = service

We pass the service into Notification instead of creating an EmailService object inside it.
Now:
- Notification can work with email or SMS.
- We can add WhatsApp notifications by creating a new class.
- We don't need to modify the Notification class when adding a new service.
This is called dependency injection: providing an object with the dependency it needs rather than making it create that dependency itself.
"""