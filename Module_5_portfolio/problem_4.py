# Mercy Oreoluwa Koku
# Nov/1/2022

# This program prints numbers 1 through 50 to the screen.
# Number are evenly divisible by that same number.

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
    elif i % 3 == 0:
        print("Your number is divisible by 3!")
    elif i % 5 == 0:
        print("Your number is divisible by 5!")

    else:
        print(i)







