from datetime import datetime

def calculate_age():
    try:
        dob = input("Enter your date of birth (DD-MM-YYYY): ")

        birth_date = datetime.strptime(dob, "%d-%m-%Y")
        today = datetime.today()

        age = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        print(f"Your age is {age} years.")

    except ValueError:
        print("Invalid date format! Please use DD-MM-YYYY.")

calculate_age()
