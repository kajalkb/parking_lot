import unittest

from parking_lot import createParkingSlots, parkVehicleinSlots, removeFromParkingSlot, showRegNoWithSameColor, showSNoWithSameColor, showSNoWithRegNumber

class testParkingLot(unittest.TestCase):
    def test_createParkingSlots(self):
        pslotlots = createParkingSlots(3)
        self.assertEqual(pslotlots.slot, 3)

    def test_parkVehicleinSlots(self):
        pslotlots = createParkingSlots(2)
        parkStMsg = parkVehicleinSlots(pslotlots, 'KA-01-HH-1234', 'White')
        parkStMsg1 = parkVehicleinSlots(pslotlots, 'KA-01-HH-1233', 'Red')
        parkStMsg2 = parkVehicleinSlots(pslotlots, 'KA-01-HH-1444', 'Yellow')
        self.assertEqual('Allocated slot number: 1', parkStMsg)
        self.assertEqual('Allocated slot number: 2', parkStMsg1)
        self.assertEqual('Sorry, parking lot is full', parkStMsg2)

    def test_removeFromParkingSlot(self):
        pslotlots = createParkingSlots(3)
        parkVehicleinSlots(pslotlots, 'KA-01-HH-1234', 'White')
        parkVehicleinSlots(pslotlots, 'KA-01-HH-1235', 'Red')
        removeMsg = removeFromParkingSlot(pslotlots, 2)
        self.assertEqual('Slot number 2 is free', removeMsg)

    def test_showRegNoWithSameColor(self):
        pslotlots = createParkingSlots(2)
        parkVehicleinSlots(pslotlots, 'KA-01-HH-1234', 'White')
        parkVehicleinSlots(pslotlots, 'KA-01-HH-1235', 'Red')
        strRegnos = showRegNoWithSameColor(pslotlots, 'White')
        self.assertEqual(strRegnos, 'KA-01-HH-1234')

    def test_showSNoWithSameColor(self):
        pslotlots = createParkingSlots(2)
        parkVehicleinSlots(pslotlots, 'KA-01-HH-1234', 'White')
        parkVehicleinSlots(pslotlots, 'KA-01-HH-1235', 'White')
        strSNos = showSNoWithSameColor(pslotlots, 'White')
        self.assertEqual(strSNos, [1, 2])

    def test_showSNoWithRegNumber(self):
        pslotlots = createParkingSlots(1)
        parkVehicleinSlots(pslotlots, 'KA-01-HH-1234', 'White')
        strSlotNo = showSNoWithRegNumber(pslotlots, 'KA-01-HH-1234')
        self.assertEqual(strSlotNo, 1)

if __name__ == '__main__':
    unittest.main()
