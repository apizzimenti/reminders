import automate
from datetime import datetime
import time

hour = datetime.now().time().hour
minute = datetime.now().time().minute

day = datetime.now().day
month = datetime.now().month
year = datetime.now().year

print("waiting...")

while True:

    hour = datetime.now().time().hour
    minute = datetime.now().time().minute

    if hour == 17 and minute == 56:
        print("it's time!")
        automate.determine_date()
        print("sleeping for a minute and a half; see you next time!")
        time.sleep(90)
