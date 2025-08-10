import datetime
import json
import random

with open('BirthdayMessages.json', 'r') as f:
    data = json.load(f)
    messages = data['Birthday messages']

birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

today=datetime.date.today()
this_year_birthday = datetime.date(today.year, birth_month, birth_day)
if this_year_birthday < today:
    next_birthday = datetime.date(today.year + 1, birth_month, birth_day)
else:
    next_birthday = this_year_birthday

days_until_birthday = (next_birthday - today).days
if days_until_birthday == 0:
    print(random.choice(messages))
else :
    print(f"Your birthday is in {days_until_birthday} days.")
