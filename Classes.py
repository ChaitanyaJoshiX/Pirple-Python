"""
Starting of program
GitHub : @ChaitanyaJoshiX
"""

class Vehicle:
    def __init__(self, Make, Model, Year, Weight, NeedsMaintenance = False, TripsSinceMaintenance = 0):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance

    def setMake(self, Make):
        self.Make = Make

    def setModel(self, Model):
        self.Model = Model

    def setYear(self, Year):
        self.Year = Year

    def setWeight(self, weight):
        self.Weight = Weight

    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

#Creating inherent class Cars from Vehicles

class Cars(Vehicle):
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance, TripsSinceMaintenance, isDriving = False):
        Vehicle.__init__(self, Make, Model, Year,Weight,NeedsMaintenance,TripsSinceMaintenance)
        self.isDriving = isDriving
    def Drive(self):
        self.isDriving = True
    def Stop(self):
        if self.isDriving == True:
            self.TripsSinceMaintenance += 1
        self.isDriving = False
        if self.TripsSinceMaintenance > 100:
            self.NeedsMaintenance = True
            print("Car needs Maintenance")

#Testing out the Cars class

#Creating i10 car and driving it a couple of times
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
i10 = Cars("Hyundai", "i10", 2011, 5000, False, 0)
i10.Drive()
i10.Stop()
print("Make :",i10.Make)
print("Model :",i10.Model)
print("Year :",i10.Year)
print("Weight :",i10.Weight,"kg")
print("Needs Maintenance ? : ",i10.NeedsMaintenance)
print("Trips Since Maintenance :",i10.TripsSinceMaintenance)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Creating scorpio car and driving it a couple of times
scorpio = Cars("Mahindra", "scorpio", 2002, 7000, False, 0)
scorpio.Drive()
scorpio.Stop()
scorpio.Drive()
scorpio.Stop()
scorpio.Drive()
scorpio.Stop()
print("Make :",scorpio.Make)
print("Model :",scorpio.Model)
print("Year :",scorpio.Year)
print("Weight :",scorpio.Weight,"kg")
print("Needs Maintenance ? : ",scorpio.NeedsMaintenance)
print("Trips Since Maintenance :",scorpio.TripsSinceMaintenance)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Creating  C-Class car and driving it a couple of times

cclass = Cars("Mercedes-Benz", "C-Class", 2020, 10000, False, 0)
cclass.Drive()
cclass.Stop()
cclass.Drive()
cclass.Stop()
cclass.Drive()
cclass.Stop()
cclass.Drive()
cclass.Stop()
cclass.Drive()
cclass.Stop()
print("Make :",cclass.Make)
print("Model :",cclass.Model)
print("Year :",cclass.Year)
print("Weight :",cclass.Weight,"kg")
print("Needs Maintenance ? : ",cclass.NeedsMaintenance)
print("Trips Since Maintenance :",cclass.TripsSinceMaintenance)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Creating inherent class Planes from Vehicles

class Planes(Vehicle):
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance, TripsSinceMaintenance, isFlying = False):
        Vehicle.__init__(self, Make, Model, Year,Weight,NeedsMaintenance,TripsSinceMaintenance)
        self.isFlying = isFlying
    def Fly(self):
        if self.NeedsMaintenance == True:
            print("The plane can't fly until it's repaired.")
            return False
        else:
            self.isFlying = True
    def Land(self):
        if self.isFlying == True:
            self.TripsSinceMaintenance += 1
        self.isFlying = False
        if self.TripsSinceMaintenance > 100:
            self.NeedsMaintenance = True
            print("Plane needs Maintenance")

#Testing out the Planes class

g650  = Planes("GulfStream", "G650", 2014, 50000, False, 99)
g650.Fly()
g650.Land()
g650.Fly()
g650.Land()
print("Make :",g650.Make)
print("Model :",g650.Model)
print("Year :",g650.Year)
print("Weight :",g650.Weight,"kg")
print("Needs Maintenance ? : ",g650.NeedsMaintenance)
print("Trips Since Maintenance :",g650.TripsSinceMaintenance)
g650.Fly()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

"""
Ending of program
GitHub : @ChaitanyaJoshiX
"""
