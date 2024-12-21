# Initialize variables
day_of_week = 1  # 1 Jan 1900 was a Monday (0 = Sunday, 1 = Monday, ..., 6 = Saturday)
sundays_on_first = 0

# Number of days in each month (non-leap year)
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Function to determine if a year is a leap year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Iterate over the years in the twentieth century
for year in range(1900, 2001):  # Include 1900 to calculate starting day for 1901
    for month in range(12):  # Iterate over each month
        if year >= 1901:  # Only count Sundays from 1901 onwards
            if day_of_week == 0:  # Sunday
                sundays_on_first += 1
        
        # Update the day of the week for the next month
        if month == 1 and is_leap_year(year):  # February in a leap year
            day_of_week = (day_of_week + 29) % 7
        else:
            day_of_week = (day_of_week + days_in_month[month]) % 7

# Output the result
print(sundays_on_first)