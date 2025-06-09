from datetime import date

def show_calendar_with_datetime():
    year = int(input("Enter year (e.g. 2025): "))
    month = int(input("Enter month (1–12): "))
    if not (1 <= month <= 12):
        print("Invalid month. Please enter 1–12.")
        return
    
    first_weekday = date(year, month, 1).weekday()
    start_day = (first_weekday + 1) % 7

   
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)
    days_in_month = (next_month - date(year, month, 1)).days

    month_name = date(year, month, 1).strftime("%B")
    print(f"     {month_name} {year}")
    print("Su Mo Tu We Th Fr Sa")


    print("   " * start_day, end="")
    day = 1
    while day <= days_in_month:
        print(f"{day:2d} ", end="")
        if (start_day + day) % 7 == 0:
            print()
        day += 1
    print() 

if __name__ == "__main__":
    show_calendar_with_datetime()
