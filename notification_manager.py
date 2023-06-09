import smtplib
import requests
from twilio.rest import Client

TWILIO_SID =
TWILIO_AUTH_TOKEN =
TWILIO_VIRTUAL_NUMBER =
TWILIO_VERIFIED_NUMBER =

my_email =
password =

class NotificationManager:

    email_list_endpoint = "https://api.sheety.co/c728fd914d4e45bec58e0ed2d09f0814/flightDeals/users"

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_email(self, message_text):
        message_text = message_text.encode('ascii', 'ignore').decode('ascii')
        response = requests.get(url=self.email_list_endpoint)
        users = response.json()["users"]
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        for user in users:
            to_email = user["email"]
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=to_email,
                                msg=f"Subject:Low price alert!\n\n{message_text}")
        connection.close()
