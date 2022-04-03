from IoTSensors import*
from Building import *


class SheridanSystem:
    def __init__(self,noOfBuild=0):
        self._nofBuildings = noOfBuild

    def invalidInput(self):
        print("Invalid Entry")
        self._nofBuildings= int(input("Re-Enter the number of buildings: ")) 
        return self._nofBuildings
        
            
           

    def run(self):
            try:
                self._nofBuildings= int(input("Enter the number of buildings: "))
            except ValueError:
                SheridanSystem.invalidInput() 
            if (self._nofBuildings <1):
                SheridanSystem.invalidInput()
            else: 
                for number in (1, self._nofBuildings + 1):
                    print("Building " , number) 
                    Building.buildingName()

    def setNofBuildings(self):
        return int( self._nofBuildings+1)



                