"""
Creating a function which adds unique elements to a list when called upon.
Adding non-unique elements to a seperate list.
Testing out the function with different elements and printing both the lists in the end.
"""
myUniqueList = [] #Creating the list for unique elements
myLeftovers = [] #Creating the list for non-unique elements
def AddToList(value):
    if value in myUniqueList:
        myLeftovers.append(value) #Adding value to non-unique list
        return False
    else:
        myUniqueList.append(value) #Adding value to unique list
        return True
print(AddToList("Hello"))
print(AddToList(1))
print(AddToList("Hello"))
print(AddToList(3.2))
print(AddToList(1))
print(myUniqueList) #Printing the unique list created
print(myLeftovers) #Printing the remaining values which were rejected in myUniqueList
