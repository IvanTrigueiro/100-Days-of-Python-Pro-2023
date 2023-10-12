from twilio.rest import Client
import os
import smtplib

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_NUMBER']
twilio_verified_number = os.environ['TWILIO_VERIFIED_NUMBER']
mail_provider_smtp_address = os.environ['MAIL_PROVIDER_SMTP_ADDRESS']
my_email = os.environ['MY_EMAIL']
my_password = os.environ['MY_PASSWORD']


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twilio_number,
            to=twilio_verified_number
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(mail_provider_smtp_address) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            for email in emails:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject: New Low Price Flight!\n\n{message}".encode("utf-8")
                )

