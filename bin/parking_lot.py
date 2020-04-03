import collections
import sys
class cars:
    def __init__(self, carRegNo, carColor):
        self.carRegNo = carRegNo
        self.carColor = carColor

class parkinglot:
    def __init__(self, slot):
        self.slot = int(slot)
        self.slots = dict.fromkeys(range(self.slot))#creating empty dictionary for given lenght
        self.pCount = 0

    def checkifSlotsAreUsedUp(self):
        counter = 0
        for i in self.slots:
            counter += 1
            #print('counter=',counter,self.)
            if (counter == self.slot):
                if(self.slots[i] == None):
                    flag = False
                else:
                    flag = True
            if(self.slot - counter > 0):
                flag = False
        return flag

    def parkCar(self, plotSlots, carDetails):
        if  self.checkifSlotsAreUsedUp():
            print('Sorry, parking lot is full')
            return

        prev = 0
        for i in list(plotSlots.slots):
            if (i - prev == 2):#inserting blank element
                j = prev+1
                d1 = {j: carDetails}
                plotSlots.slots.update(d1)
                plotSlots.slots = collections.OrderedDict(sorted(plotSlots.slots.items()))
                print ('Allocated slot number: ', j+1)
                return

            if plotSlots.slots[i] == None:
                plotSlots.slots[i] = carDetails
                print ('Allocated slot number: ', i+1)
                break
            prev = i


    def removeACar(self, sNumber):
        self.slots.pop(sNumber)
        print ('Slot number ',int(sNumber)+1,' is free ')

    def status(self):
        print('Slot No.      ','Registration No','     Colour')
        for i in self.slots:
            j = i+1
            print(j,'           ',self.slots[i].carRegNo,'             ',self.slots[i].carColor,'     ')

    def regNowithColor(self, scolor):
        regNos = ''
        listRegNo = []
        for i in self.slots:
            if self.slots[i].carColor == scolor:
                    listRegNo.append(self.slots[i].carRegNo)
        print(', '.join(listRegNo))

    def sNowithColor(self, scolor):
        sNos = ''
        listSNo = []
        for i in self.slots:
            if self.slots[i].carColor == scolor:
                    listSNo.append(i+1)
        print(*listSNo, sep = ", ")

    def sNowithRegNo(self, carRNo):
        carFound = False
        for i in self.slots:
            if self.slots[i].carRegNo == carRNo:
                carFound = True
                print(i+1)
        if not carFound :
            print('Not found')

class ticket:
    def __init__(self, slot, car):
        self.slot = slot
        self.car = car

def createParkingSlots(noOfslots):
    plotSlots = parkinglot(noOfslots)
    print('Created a parking lot with ', noOfslots ,' slots')
    return plotSlots

def parkVehicleinSlots(plotSlots, carRegNo, carColor):
    carDetails = cars(carRegNo, carColor)
    plotSlots.parkCar(plotSlots, carDetails)
    #return "Parking Successful"

def removeFromParkingSlot(plotSlots, sNumber):
    plotSlots.removeACar(int(sNumber)-1)

def showStatus(plotSlots):
    plotSlots.status()

def showRegNoWithSameColor(plotSlots, scolor):
    plotSlots.regNowithColor(scolor)

def showSNoWithSameColor (plotSlots, scolor):
    plotSlots.sNowithColor(scolor)

def showSNoWithRegNumber (plotSlots, carRNo):
    plotSlots.sNowithRegNo(carRNo)

def cmdInterpretor(plotSlots, parkingCommand):

    cmdline = parkingCommand.split()

    if(cmdline[0] == 'create_parking_lot'):
        plotSlots = createParkingSlots(cmdline[1])
    elif(cmdline[0] == 'park'):
        parkVehicleinSlots(plotSlots, cmdline[1], cmdline[2])
    elif(cmdline[0] == 'leave'):
        removeFromParkingSlot(plotSlots, cmdline[1])
    elif(cmdline[0] == 'status'):
        showStatus(plotSlots)
    elif(cmdline[0] == 'registration_numbers_for_cars_with_colour'):
        showRegNoWithSameColor(plotSlots, cmdline[1])
    elif(cmdline[0] == 'slot_numbers_for_cars_with_colour'):
        showSNoWithSameColor(plotSlots, cmdline[1])
    elif(cmdline[0] == 'slot_number_for_registration_number'):
        showSNoWithRegNumber(plotSlots, cmdline[1])
    else:
        print('Invalid command.')

    return plotSlots

def exeCuteInteractively():#commands :create_parking_lot,park,leave,status, exit etc
    cmdline = input().split()

    while(cmdline[0] != 'exit'):
        if(cmdline[0] == 'create_parking_lot'):
            plotSlots = createParkingSlots(cmdline[1])
        elif(cmdline[0] == 'park'):
            parkVehicleinSlots(plotSlots, cmdline[1], cmdline[2])
        elif(cmdline[0] == 'leave'):
            removeFromParkingSlot(plotSlots, cmdline[1])
        elif(cmdline[0] == 'status'):
            showStatus(plotSlots)
        elif(cmdline[0] == 'registration_numbers_for_cars_with_colour'):
            showRegNoWithSameColor(plotSlots, cmdline[1])
        elif(cmdline[0] == 'slot_numbers_for_cars_with_colour'):
            showSNoWithSameColor(plotSlots, cmdline[1])
        elif(cmdline[0] == 'slot_number_for_registration_number'):
            showSNoWithRegNumber(plotSlots, cmdline[1])

        else:
            break
        cmdline = input().split()
    return


def exeCuteWithFileInputs(plotSlots, inCmdFile):
    f = open(inCmdFile, "r")
    while (True):
        cmds = f.readline()
        if cmds == '':
            break
        plotSlots = cmdInterpretor(plotSlots, cmds)


def initialize(plotSlots):
    if len(sys.argv) == 2:
        exeCuteWithFileInputs(plotSlots, sys.argv[1])#call with the file name
    else:
        exeCuteInteractively()

def main():
    #print('test')
    initialize(None)


if __name__ == '__main__':
    main()
