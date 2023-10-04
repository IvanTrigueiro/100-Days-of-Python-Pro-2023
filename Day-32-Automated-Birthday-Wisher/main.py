import smtplib
import datetime as dt
from random import randint
import pandas as pd

##################### Extra Hard Starting Project ######################
sender_email = "contatesteparaprogramar@outlook.com"
sender_pass = "essaehumasenhateste23"

# 1. Update the birthdays.csv # Done
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_month = now.month
current_day = now.day
birthdays = pd.read_csv("birthdays.csv")
birthdays_dict = birthdays.to_dict(orient="records")

for birthday in birthdays_dict:
    if birthday["month"] == current_month and birthday["day"] == current_day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        receiver_email = birthday["email"]
        letter_number = randint(1, 3)
        with open(f"letter_templates/letter_{letter_number}.txt") as letter:
            letter_contents = letter.read()
            letter_contents = letter_contents.replace("[NAME]", birthday["name"])
# 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.office365.com", port=587) as connection:
                connection.starttls()
                connection.login(user=sender_email, password=sender_pass)
                connection.sendmail(
                    from_addr=sender_email,
                    to_addrs=receiver_email,
                    msg=f"Subject:Happy Birthday!\n\n{letter_contents}"
                )
