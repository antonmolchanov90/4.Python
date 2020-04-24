"""
Final Project for course "Python Programming Essentials"
4 functions to process dates.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month==12:
        return 31
    else:
        date1 = datetime.date(year, month, 1)
        date2 = datetime.date(year, month+1, 1)
        difference = date2 - date1
        return(difference.days) 
print(days_in_month(2018,2))

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if datetime.MINYEAR<=year<=datetime.MAXYEAR and 1<=month<=12 and 1<=day<= days_in_month(year, month):
        return True
    else:
        return False
print(is_valid_date(2018,10,21))

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    date1=datetime.date(year1,month1,day1)
    date2=datetime.date(year2,month2,day2)
    if is_valid_date(year1,month1,day1) and is_valid_date(year2,month2,day2)and (date1<date2):
        difference=date2-date1
        print(difference.days)
        return difference.days

    else:        
        return 0 


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day
 
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    test_date = True
   
    if test_date == is_valid_date(year, month, day):
 
        date_given =  datetime.date(year, month, day)
        date_today = datetime.date.today()
       
        if date_given > date_today:
            return False
        else:
           
            number_of_days_between = date_today - date_given
            return (number_of_days_between.days)
       
    else:
   
        return False