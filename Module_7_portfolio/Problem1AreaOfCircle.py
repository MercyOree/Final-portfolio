# Mercy O. koku
# Nov/15/2022
# Problem 1 is about how to wirte a function areaOfCircle(r) which returns the area of a circle of radius r.

# This code will write a function areaOfCircle(r)
import math
def area_of_circle(r):
    area_of_circle = r * r * math.pi
    return area_of_circle
r = float(input("Enter a radius of your circle: "))
result = area_of_circle (r)
print ("The area of the circle is", result)