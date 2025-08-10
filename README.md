# 🎉 Birthday Countdown & Message Script

This Python script helps you count down the days to your next birthday and gives you a random celebratory message on the special day!  
Birthday messages are loaded from a JSON file and shown only when it's your birthday.

## 📦 Features

- **User-Friendly:** Prompts for your birth month and day.
- **Countdown:** Tells you how many days remain until your next birthday.
- **Surprise!:** On your birthday, you receive a randomly selected message from a customizable set.
- **Easy Customization:** Messages are stored in a simple JSON file for easy editing.

## 📝 Requirements

- Python 3.x

## 💾 Setup

1. **Clone this repository or copy the script files.**
2. **Ensure you have a `BirthdayMessages.json` file** in the same directory as the script.  
   Example `BirthdayMessages.json`:
   ```json
   {
       "Birthday messages": [
           "Happy Birthday! 🎂",
           "Wishing you a fantastic birthday!",
           "Another year older, another year wiser. Happy Birthday!",
           "Hope your birthday is as awesome as you are!"
       ]
   }
   ```
3. **Run the script:**
   ```bash
   python birthday_script.py
   ```

## 🚀 Usage

1. When prompted, enter your birth month (as a number from 1 to 12).
2. Enter your birth day (as a number from 1 to 31).
3. The script will:
    - Tell you how many days until your next birthday, **or**
    - If today is your birthday, show you a random birthday message.

## 🧑‍💻 Code Overview

```python
import datetime
import json
import random

with open('BirthdayMessages.json', 'r') as f:
    data = json.load(f)
    messages = data['Birthday messages']

birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

today = datetime.date.today()
this_year_birthday = datetime.date(today.year, birth_month, birth_day)
if this_year_birthday < today:
    next_birthday = datetime.date(today.year + 1, birth_month, birth_day)
else:
    next_birthday = this_year_birthday

days_until_birthday = (next_birthday - today).days
if days_until_birthday == 0:
    print(random.choice(messages))
else:
    print(f"Your birthday is in {days_until_birthday} days.")
```

## ✍️ Customizing Messages

To add or edit birthday messages, simply update the `"Birthday messages"` array in `BirthdayMessages.json`.

## 📄 License

This project is open source and free to use for educational and personal purposes.

---

Happy coding,  
**Raccoon** 