# Mercy O. koku
# Nov/29/2022
# Problem 4 is about how to write a function that takes a year as a parameter.
# Which returns using true and false statements.


def isLeapYear(year):
    if year %4 == 0: #checks if this year is divisible by 4
        if year % 100 == 0: #if it is, checks if divisible by 100
          if year % 400 == 0: #if it is too, checks if divisible by 400
              return True #year is divisible by 4
          else:
              return False #year is divisible by 100 but not 400
        else:
            return True #year is divisble by 4 but not 100
    else:
        return False #year is not divisible by 4

year = int(input("Enter in a year"))


print(isLeapYear(year))
print(isLeapYear(503))

