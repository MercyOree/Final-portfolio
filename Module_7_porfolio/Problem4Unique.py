# Mercy O. koku
# Nov/15/2022
# Problem 4 is about how to write a function that takes a list of numbers
# Returns a new list with unique elements of the first list.

#This code will write a function that returns a new list with unique elements of the first list.
def unique_list(l):
    mylist = [2,2,4,4,6,6,8,3,6,6,5,7]
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x
print("The unique list of 2,2,4,4,6,6,8,3,6,6,5,7 ")
print(unique_list([2,2,4,4,6,6,8,3,6,6,5,7]))