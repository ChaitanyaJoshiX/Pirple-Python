"""
Handle the errors using try and except.
Use any function you like.
"""
Things = ["Chocolate", "Chips", "Apple", "Water"]
l = len(Things)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\t\tGENERAL STORES PVT. LTD")
print("\t\t    ITEMS FOR SALE")
for i in range(1,l+1):
    print(i,":",Things[i-1])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
inp = int(input("What would you like to buy? : "))
try:
    print("Bought 1",Things[inp-1])
    print("Good Day! ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
except Exception as exep:
    print(exep)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
