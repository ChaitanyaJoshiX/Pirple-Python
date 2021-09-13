"""
Takes a integer list as input from user
Sorts the list.
display list in ascending order after sorting.
"""
list =[]
print("````````````````````````````````````````````````````")
print("Welcome to the list sorting program! Lets begin.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
l = int(input("How many numbers will there be in your list? : "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Enter your numbers one by one.")
for i in range(l):
    temp = float(input("Enter number "+str(i+1)+" : "))
    list.append(temp)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Original list :",list)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
list.sort()
print("Your Sorted List in ascending order :",list)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
