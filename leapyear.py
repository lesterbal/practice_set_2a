def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"

try:
    input_year = int(input('\n:: Enter year: '))
    print(is_leap_year(input_year))
except ValueError:
    print('[!] Please enter a valid year!')
