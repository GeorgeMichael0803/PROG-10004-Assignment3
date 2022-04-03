from IoTSensors import*

class Building:
    def __init__(self,buildName="" ,noOfSensors=0, listOfSensors=[]):
        self._noOfSensors = noOfSensors
        self._listOfSensors= listOfSensors
        self._buildName = buildName


    def buildingName(self):
        self._buildName = input("Enter the building name: ") 

        if self._buildName.isnumeric() == True:
            print("Invalid Entry")
            self._buildName = input("Re-Enter the building name [No numbers]: ")


    def sensorNo(self):
        try:         
            self._noOfSensors =int(input("Enter the number of sensors deployed accross Sheridan Campus: "))
        except ValueError:
            print("Invalid Input, please type an integer") 
            Building.sensorNo()                                                
                                                                                                
        if (self._noOfSensors<1 ):
            print("Invalid Input, please type a positive number ")
            Building.sensorNo()
        else:
            pass
        
                  


    def setSensorNo(self):
        return int(self._noOfSensors ) 


    def setNoOfSensors(self):
        return int(self._noOfSensors  +1)  

    def setBuildName(self):
        return self._buildName 

            




        
