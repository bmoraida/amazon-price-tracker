import os
import smtplib


class EmailHandler:
    def __init__(self):
        self.user = os.environ.get("EMAIL_USER")
        self.password = os.environ.get("EMAIL_PASSWORD")
        self.email_host = os.environ.get("EMAIL_HOST")
        self.to_email = os.environ.get("TO_EMAIL")

    def send_price_notification(self, message):
        with smtplib.SMTP(self.email_host, port=587) as connection:
            connection.starttls()
            connection.login(user=self.user, password=self.password)
            connection.sendmail(
                from_addr=self.user,
                to_addrs=self.to_email,
                msg=f"Subject:Price Alert!\n\n{message}",
            )
