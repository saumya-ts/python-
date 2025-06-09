import calendar

def show_calendar():
    year = int(input("Enter year (e.g. 2025): "))
    month = int(input("Enter month (1–12): "))
    if 1 <= month <= 12:
        print(calendar.month(year, month))
    else:
        print("Invalid month. Please enter a value between 1 and 12.")

if __name__ == "__main__":
    show_calendar()
