'''# Python program to check if year is a leap year or not

year = 2025

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))'''

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # 能被400整除的年份是閏年
            else:
                return False  # 能被100整除但不能被400整除的年份不是閏年
        else:
            return True  # 能被4整除但不能被100整除的年份是閏年
    else:
        return False  # 不能被4整除的年份不是閏年

# 測試例子
year = 2023
if is_leap_year(year):
    print(f"{year}年是閏年")
else:
    print(f"{year}年不是閏年")

