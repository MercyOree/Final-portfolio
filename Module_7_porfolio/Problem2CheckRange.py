# Mercy O. koku
# Nov/15/2022
# Problem 2 is about how to write a function that has a paramter checking to see whether a number is between 1 and 10 with true or false statements.

# This code will writes a function that takes a number as a parameter.
# This function will also give a true statment if between 1 and 10 and false if not between 1 and 10.

def test_range(n):
    if n>=1 and n<=10:
        print(n," is between 1 and 10, your number is True")
    else:
        print(n," is not between 1 and 10, your number is False")


test = int(input("Enter in a number between 1 and 10 "))

test_range(test)




