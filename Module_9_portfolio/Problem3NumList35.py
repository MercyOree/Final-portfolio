#Mercy O. koku
#Dec/6/2022
# Problem 3 a user use a while loop, ask the user to enter a number.
# Each number enter creates a list added together until greater than 100.
print("Enter in a list of numbers when added together is greater than 100")
print("When you finish entering your number type 'done' into 'Please enter a number:' ")
a = []
total = 0
while True:
    list = input("Please enter a number for your list: ")
    if list== "done":
        break
    list = int(list)
    a.append(list)
list= sum(a)
print(list>=100,a)