import smtplib
import datetime as dt
from random import choice

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:
    with open("quotes.txt") as quotes_data:
        all_quotes = quotes_data.readlines()
        all_quotes = [q.strip() for q in all_quotes]
        random_quote = choice(all_quotes)

        # for Outlook e-mail
        first_account = "contatesteparaprogramar@outlook.com"
        second_account = "essaehareceiver@outlook.com"
        first_pass = "essaehumasenhateste23"

        with smtplib.SMTP("smtp.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(user=first_account, password=first_pass)
            connection.sendmail(
                from_addr=first_account,
                to_addrs=second_account,
                msg=f"Subject:Happy Week \n\n{random_quote}")
