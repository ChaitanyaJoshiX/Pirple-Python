"""
This program is menu driven.
Library chosen to be used extensively is math module.
GitHub : @ChaitanyaJoshiX
"""
import math
def MathFunctions():

    if choice == 1:
        n = float(input("Enter the number you want to perform the floor operation on : "))
        print(math.floor(n))

    elif choice == 2:
        n = float(input("Enter the number you want to perform the ceil operation on : "))
        print(math.ceil(n))

    elif choice == 3:
        n = float(input("Enter the number you want the factorial of : "))
        print(math.factorial(n))

    elif choice == 4:
        n = float(input("Enter the number you want the square root of : "))
        print(math.sqrt(n))

    elif choice == 5:
        n = float(input("Enter the number (x) :  "))
        power = int(input("Enter the power you want the number to be raised to (y)  : "))
        print(math.pow(n,power))

    elif choice == 6:
        angle = float(input("Enter the angle in radians : "))
        print(math.degrees(angle),"rad")

    elif choice == 7:
        angle = float(input("Enter the angle in degrees : "))
        print(math.radians(angle),"°")

    elif choice == 8:
        n = math.pi
        print("var n initialised with pi = ",n)

    elif choice == 9:
        n = math.e
        print("var n initialised with e = ",n)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\t\tMenu : ")
print("1 : Round number down (floor)\n2 : Round number up (ceil)\n3 : factorial")
print("4 : Square Root\n5 : Power (x to the power y)\n6 : convert to degrees (from radians)")
print("7 : convert to radians (from degrees)\n8 : initialise with constant pi")
print("9 : initialise with constant e")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
choice = int(input("Enter your choice (1,2,3,4,5,6,7,8,9) : "))
MathFunctions()
"""
GitHub : @ChaitanyaJoshiX
"""
