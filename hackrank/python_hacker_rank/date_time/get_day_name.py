import calendar

if __name__ == "__main__":
    month, date, year = list(map(int, input().split()))
    day = calendar.weekday(year, month, date)
    day_name = list(calendar.day_name)

    print(day_name[day].upper())