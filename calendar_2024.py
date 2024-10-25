import calendar

def create_calendar_for_2024():
    # Create a text file to store the calendar
    with open("calendar_2024.txt", "w") as f:
        # Loop over each month of the year 2024
        for month in range(1, 13):
            # Get the month calendar as a string
            month_calendar = calendar.month(2024, month)
            # Write the month calendar to the file
            f.write(month_calendar + "\n")
        print("Calendar for 2024 has been created and saved to calendar_2024.txt")

if __name__ == "__main__":
    create_calendar_for_2024()
