"""
Writing a Function that accepts 3 parameters
Checks for equality between any two of them or more
"""
def CheckEqual(a, b, c):
    a, b, c = int(a), int(b), int(c)
    if a == b:
        print("True\na = b")
    if b == c:
         print("True\nb = c")
    if a == c:
        print("True\na = c")
    else:
        print("False")
CheckEqual(5, 6, "6") #Testing out the function with an example
