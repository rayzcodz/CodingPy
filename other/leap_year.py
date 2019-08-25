# WAP that calculates whether a given year is a leap year or not.
# Every year that is exactly divisible by four is a leap year,
#     except for years that are exactly divisible by 100,
#         but these centurial years are leap years if they are exactly divisible by 400.
#
# For example, the years 1700, 1800,
# and 1900 are not leap years, but the years 1600 and 2000 are.

def is_leap_year(year):
    is_leap_year = False
    if year % 4 == 0:
        is_leap_year = True
        if year % 100 == 0:
            is_leap_year = False
            if year % 400 == 0:
                is_leap_year = True
    return is_leap_year

# Below list contains some of the leap years. I will write a program to verify it.
leap_years = [2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]
for year in leap_years:
    result = '{} is leap year {}'.format(year, is_leap_year(year))
    print(result)