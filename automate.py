import datetime
import csv
import smtplib
from email.mime.text import MIMEText


def determine_date():

    steve = "steven-tomblin@uiowa.edu"
    me = "anthony-pizzimenti@uiowa.edu"

    day = datetime.date.today().day
    month = datetime.date.today().month
    year = datetime.date.today().year

    with open("dates.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            pay_day = row["day"]
            pay_month = row["month"]
            pay_year = row["year"]

            days = day == pay_day
            months = month == pay_month
            years = year == pay_year

            if days and months and years:
                send_mail(steve, day, month, year)


def send_mail(recipient, day, month, year):

    with open("steve_message.txt", "r") as file:
        steve_message = file.read().format(month, day, year)

    with open("me_message.txt", "r") as file:
        me_message = file.read().format(month, day, year)

    email = MIMEText(steve_message)
    email["Subject"] = "Timesheet Reminder"
    email["From"] = "anthony-pizzimenti@uiowa.edu"
    email["To"] = recipient

    s = smtplib.SMTP("localhost")
    s.send_message(email)

    memail = MIMEText(me_message)
    memail["Subject"] = "reminder is working"
    memail["From"] = "anthony-pizzimenti@uiowa.edu"
    memail["To"] = "anthony-pizzimenti@uiowa.edu"

    s.send_message(memail)
    s.quit()
