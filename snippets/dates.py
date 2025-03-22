from datetime import date

# Get today's date
today = date.today()
print("Today's date:", today)  # Output: Today's date: YYYY-MM-DD (e.g., 2023-10-05)

# Create a specific date
specific_date = date(2023, 10, 5)
print("Specific date:", specific_date)  # Output: Specific date: 2023-10-05

# Accessing year, month, and day
year = today.year
month = today.month
day = today.day
print(f"Year: {year}, Month: {month}, Day: {day}")  # Output: Year: YYYY, Month: MM, Day: DD

       