"""
Writing a program that prints the numbers from 1 to 100.
But, for multiples of three printing "Fizz".
For multiples of five printing "Buzz".
For multiples of both three and five printing "FizzBuzz".
If a number is prime printing "Prime"
"""
for i in range(1,101):
    s = 0
    if i == 1:
        print(i)
        continue
    k = True
    for j in range(1,i+1):
        if i % j == 0:
            s += 1
    if s == 2:
        print("Prime")
        continue
    if i % 3 == 0 and i % 5 == 0: #Checking if the number is divisible by 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0: #Checking if the number is divisible by 3
        print("Fizz")
    elif i % 5 == 0: #Checking if the number is divisible by 5
        print("Buzz")
    else:
        print(i)
