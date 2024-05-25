import time # used to simulate the time passing (optional - now commented out)

def gen_secs():
    """
    This function returns a generator for all the seconds in a minute
    """
    for second in range(60):
        yield second

def gen_minutes():
    """
    This function returns a generator for all the minutes in a hour
    """
    for minute in range(60):
        yield minute

def gen_hours():
    """
    This function returns a generator for all the hours in a day
    """
    for hours in range(24):
        yield hours


def gen_time():
    """
    This function returns a generator for all the hours, minutes and seconds in a day
    """
    for hours in gen_hours(): # Loop through all the hours in a day
        for minutes in gen_minutes(): # Loop through all the minutes in a hour
            for seconds in gen_secs(): # Loop through all the seconds in a minute
                # Return the time in the format HH:MM:SS
                yield "%02d:%02d:%02d" % (hours, minutes, seconds)
                # Sleep for 1 seconds to simulate the time passing
                # time.sleep(1)

def gen_years(start=2024):
    """
    This function returns a generator for all the years starting from the given year
    """
    while True:
        yield start
        start += 1

def gen_months():
    """
    This function returns a generator for all the months in a year
    """
    for month in range(1, 13):
        yield month

def gen_days(month, leap_year=False):
    """
    This function returns a generator for all the days in a month
    :param month: The month for which the days are to be generated
    :param leap_year: A boolean value indicating if the year is a leap year
    """
    # days in each month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # If it is a leap year, update the days in February
    if leap_year:
        days_in_month[1] = 29
    # Loop through all the days in the month
    for day in range(1, days_in_month[month - 1] + 1):
        yield day


def gen_date():
    """
    This function returns a generator for all the years, months, days and time in a year
    """
    for year in gen_years(): # Loop through all the years
        for month in gen_months(): # Loop through all the months
            # Check if the year is a leap year
            leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            for day in gen_days(month, leap_year): # Loop through all the days
                for time in gen_time(): # Loop through all the time
                    # Return the date in the format DD-MM-YYYY HH:MM:SS
                    yield "%02d-%02d-%04d %s" % (day, month, year, time)

def every_million():
    """
    print the output of gen_date every millionth time
    """
    everymillion  = 0
    for gd in gen_date():
        if everymillion % 1000000 == 0:
            print(gd)
        everymillion += 1


def main():
    # if you want to see output in real time speed uncomment the time.sleep(1) in gen_time function.
    # if you want to see output faster you can comment the time.sleep(1) in gen_time function.
    every_million()


if __name__ == "__main__":
    main()