import sys
import collections

# Contains the car registration number and colour
# This helps us to create instance of multiple cars parked
class cars:
    def __init__(self, carRegNo, carColor):
        self.carRegNo = carRegNo
        self.carColor = carColor

# Parking lot used to contains the slot information against
# multiple cars being parkedCar
class parkinglot:
    def __init__(self, slot):
        self.slot = int(slot)
        self.slots = dict.fromkeys(range(self.slot))#creating empty dictionary for given lenght

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
            sinfoMsg = 'Sorry, parking lot is full'
            print('Sorry, parking lot is full')
            return sinfoMsg

        prev = 0
        for i in list(plotSlots.slots):
            if (i - prev == 2):#inserting blank element
                j = prev+1
                plotSlots.slots[j]=carDetails
                #sort the listS
                plotSlots.slots = collections.OrderedDict(sorted(plotSlots.slots.items()))
                sinfoMsg = 'Allocated slot number: ' + str(j+1)
                print ('Allocated slot number:', j+1)
                return sinfoMsg

            if plotSlots.slots[i] == None:
                plotSlots.slots[i] = carDetails
                sinfoMsg = 'Allocated slot number: ' + str(i+1)
                print ('Allocated slot number:', i+1)
                return sinfoMsg
            prev = i


    def removeACar(self, sNumber):
        self.slots.pop(sNumber)
        print ('Slot number', int(sNumber)+1 ,'is free')
        strRemoveMsg = 'Slot number ' + str(int(sNumber)+1) + ' is free'
        return strRemoveMsg

    def status(self):
        print('Slot No.   ','Registration No','   Colour')
        for i in self.slots:
            j = i+1
            print(j,'         ',self.slots[i].carRegNo,'    ',self.slots[i].carColor)

    def regNowithColor(self, scolor):
        regNos = ''
        listRegNo = []
        for i in self.slots:
            if self.slots[i].carColor == scolor:
                    listRegNo.append(self.slots[i].carRegNo)
        print(', '.join(listRegNo))
        return listRegNo

    def sNowithColor(self, scolor):
        sNos = ''
        listSNo = []
        for i in self.slots:
            if self.slots[i].carColor == scolor:
                    listSNo.append(i+1)
        print(*listSNo, sep = ", ")
        return listSNo

    def sNowithRegNo(self, carRNo):
        carFound = False
        for i in self.slots:
            if self.slots[i].carRegNo == carRNo:
                carFound = True
                print(i+1)
                return i+1
        if not carFound :
            print('Not found')

class ticket:
    def __init__(self, slot, car):
        self.slot = slot
        self.car = car

# creates parking slot based on the number of get_slots
# passed to it
def createParkingSlots(noOfslots):
    plotSlots = parkinglot(noOfslots)
    print('Created a parking lot with', noOfslots ,'slots')
    return plotSlots

# parks the car to the nearest slot from the start
def parkVehicleinSlots(plotSlots, carRegNo, carColor):
    carDetails = cars(carRegNo, carColor)
    parkStMsg = plotSlots.parkCar(plotSlots, carDetails)
    return parkStMsg

# Removes the car from the slot number in the
# parking lot
def removeFromParkingSlot(plotSlots, sNumber):
    strRemoveMsg = plotSlots.removeACar(int(sNumber)-1)
    return strRemoveMsg

# Displays status of parking lot with slot number ,
# car number and color in an order
def showStatus(plotSlots):
    plotSlots.status()

# Displays registraton number of the cars whose colour is
# provided
def showRegNoWithSameColor(plotSlots, scolor):
    strRegnos = plotSlots.regNowithColor(scolor)
    return ', '.join(strRegnos)

# Displays slot number of the cars whose colour is
# provided
def showSNoWithSameColor (plotSlots, scolor):
    strSNo = plotSlots.sNowithColor(scolor)
    return strSNo

# Displays slot number of whose registration number is
# provided
def showSNoWithRegNumber (plotSlots, carRNo):
    strSlotNo = plotSlots.sNowithRegNo(carRNo)
    return strSlotNo

# Interprates the command from the command line or from the file input
# and runs the command accordintly
def cmdInterpretor(plotSlots, parkingCommand , cmdMode):

    #adding the following condition as list does
    #not have a split() in interactive mode for parkingCommand
    if(cmdMode == 'fMode'):
        cmdline = parkingCommand.split()
    else:
        cmdline = parkingCommand

    if not cmdline[0] == 'create_parking_lot':
        if plotSlots == None:
            print('Parking slot is not initialized. Please use create_parking_lot to get started.')
            return

    if(cmdline[0] == 'create_parking_lot'):
        plotSlots = createParkingSlots(cmdline[1])
    elif(cmdline[0] == 'park'):
        parkVehicleinSlots(plotSlots, cmdline[1], cmdline[2])
    elif(cmdline[0] == 'leave'):
        if plotSlots :
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

# Reads the commands from a input file (txt format) and calls
# cmdInterpretor to run them one by one till the end of the file is met
def exeCuteWithFileInputs(plotSlots, inCmdFile):
    f = open(inCmdFile, "r")
    while (True):
        cmds = f.readline()
        if cmds == '':
            break
        plotSlots = cmdInterpretor(plotSlots, cmds, 'fMode')#fMode is for file input mode
    return

# Reads the command individually via the input() function and calls
# cmdInterpretor to run them one by one till exit is passed
def exeCuteInteractively(plotSlots):
    cmdline = input().split()

    while(cmdline[0] != 'exit'):
        plotSlots = cmdInterpretor(plotSlots, cmdline,'iMode')#iMode is for interactive mode
        cmdline = input().split()
    return

# The initialize function will parse arguments via the parser variable.  These
# arguments will be defined by the user on the console. Either its a filename
# or a inidividual command
def initialize(plotSlots):
    if len(sys.argv) == 2:
        exeCuteWithFileInputs(plotSlots, sys.argv[1])#call with the file name
    else:
        exeCuteInteractively(plotSlots)
    return

# The main function calls the initialize function and passes None to
# initilize parkingLot class object
def main():
    initialize(None)


if __name__ == '__main__':
    main()
