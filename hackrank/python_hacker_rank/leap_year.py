def is_leap(year):
    leap = False
    if 1900<= year<=100000:
        if (year % 4 == 0 and year % 100 != 0 and year % 400 == 0):
            leap = True
    return leap



year = int(input())
print(is_leap(year))
# challageing to undersatnd
# Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100,
# but these centurial years are leap years if they are exactly divisible by 400.
# For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.
