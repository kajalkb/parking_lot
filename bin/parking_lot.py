import collections

class cars:
    def __init__(self, carRegNo, carColor):
        self.carRegNo = carRegNo
        self.carColor = carColor

class parkinglot:
    def __init__(self, slot):
        self.slot = slot
        self.slots = dict.fromkeys(range(self.slot))#creating empty dictionary for given lenght

    def checkifSlotsAreUsedUp():
        for i in self.slots:
            if self.slots[i] == None:
                return false
        return true

    def parkCar(self, plotSlots, carDetails):
        '''if self.checkifSlotsAreUsedUp :
            print ('slots are full')'''
        prev = 0
        for i in list(plotSlots.slots):
            if i - prev == 2 :#inserting blank element
                j = prev+1
                d1 = {j: carDetails}
                plotSlots.slots.update(d1)

            if plotSlots.slots[i] == None:
                plotSlots.slots[i] = carDetails
                break
            prev = i
            #sort the dictionary
        plotSlots.slots = collections.OrderedDict(sorted(plotSlots.slots.items()))

        print ('Allocated slot number: ', i+1)


    def removeACar(self, sNumber):
        #self.slots[sNumber].carRegNo = None
        #self.slots[sNumber].carColor = None
        self.slots.pop(sNumber)

        #for i in self.slots:
            #print(self.slots[i].carColor)

    def status(self):
        print('Slot No.      ','Registration No','     Colour')
        for i in self.slots:
            j = i+1
            print(j,'           ',self.slots[i].carRegNo,'             ',self.slots[i].carColor,'     ')

class ticket:
    def __init__(self, slot, car):
        self.slot = slot
        self.car = car

def createParkingSlots(noOfslots):
    plotSlots = parkinglot(noOfslots)
    return plotSlots

def parkVehicleinSlots(plotSlots, carRegNo, carColor):
    carDetails = cars(carRegNo, carColor)
    plotSlots.parkCar(plotSlots, carDetails)
    #return "Parking Successful"

def removeFromParkingSlot(plotSlots, sNumber):
    plotSlots.removeACar(sNumber-1)
    return "Remove successful"

def showStatus(plotSlots):
    plotSlots.status()

#starting of program
noOfslots = 5
carRegNo = "KA-1234"
carColor = "White"
sNo = 4
plotSlots = createParkingSlots(noOfslots)
parkVehicleinSlots(plotSlots, carRegNo, carColor)
parkVehicleinSlots(plotSlots, "MH-3456", "RED")
parkVehicleinSlots(plotSlots, "KL-1999", "Orange")
parkVehicleinSlots(plotSlots, "WB-9876", "White")
parkVehicleinSlots(plotSlots, "MH-1111", "White")

print(removeFromParkingSlot(plotSlots, 4))
print(plotSlots.slots)

#showStatus(plotSlots)

#parkVehicleinSlots(plotSlots, "WB-9876", "White")
#showStatus(plotSlots)
