import random

from Building import Building
from SheridanSystem import * 

class Sensors:
    def __init__(self, posX, posY, noDays, avgRead, co2Levels,avgCo2Levels,):
        self._posX= posX
        self._posY = posY
        self._noDays = noDays
        self._avgRead = avgRead
        self._co2Levels= co2Levels
        self._avgCo2Levels= avgCo2Levels
        

    def sensorPos(self):
                                                      
        coordinate =  round(random.uniform(0.00, 100.00), 2)       
        return coordinate

    def sensorReading(self):
        self._noDays=input("Enter the number of days for the readings: ")           
        self._noDays=int(self._noDays)                                                      
        self._co2Levels=[]
        self._avgCo2Levels = []
        for i in range (1, self._noDays+1): 
            data=(input("Enter the CO2 for Day "+ str(i)+ ": "))
            self._co2Levels.append(data)   
            for j in range (1, self._noDays+1):
                Sensors.computeAvg()
                j+=1
        

    def computeAvg(self):
            for counter1 in self._co2Levels:  
                sumOfCO2= sumOfCO2 + int(counter1)
                self._avgCo2Levels.append(sumOfCO2)


class Co2Sensors(Sensors, Building, SheridanSystem):
    def __init__(self, posX, posY, noDays, avgRead,co2Levels,avgCo2Levels, coordinate ):
        super().__init__( posX, posY, noDays, avgRead, co2Levels,avgCo2Levels, coordinate)



    def printInfo(self):
        for value in (1, SheridanSystem.nofBuildingsReturn()):
            print("This is for Building: " , self._buildName)
            for range in (0, Building.sensorNoReturn()):
                print("x:" , Sensors.sensorPos())
                print("y:", Sensors.sensorPos())
                for var in (0, self._noDays):
                    print("Day:", var+1 ,self._co2Levels[var] )
                print("Average Reading(s):" , self._avgCo2Levels[range])       
        
