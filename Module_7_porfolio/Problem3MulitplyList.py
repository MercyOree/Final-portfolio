# Mercy O. koku
# Nov/15/2022
# Problem 3 is about how to write a function to multiply all the numbers in a list.

#This code will write a function that multiples all the numbers in a list

def Multiplylist(my_list):
    r = 1
    for a in my_list:
        r = r * a
    return r
list = [2,4,6,7,14]
print("List: 2,4,6,7,14")
print("Multiplication of list: ", Multiplylist(list))
