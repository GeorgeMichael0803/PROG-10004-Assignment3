from Building import *
from IoTSensors import * 
from SheridanSystem import *


class Application:
    def start(self):
        SheridanSystem.run()
        Building.sensorNo()
        for counter in (1,Building.setNoOfSensors() ):
                print("Sensor ", counter) 
                Sensors.sensorReading()
        Co2Sensors.printInfo()
        Application.continuation()





    def continuation():   
        reply= input("Do you want to contine: (Y)es or (N)o: ")
        if (reply=="Yes" or reply=="yes" or reply=="Y" or reply=="y" ): 
               Application.start()                                                          
        elif(reply=="No" or reply=="no" or reply=="N" or reply=="n"):
            print("Existing the Program......")   
            quit()                        
        else: 
            print("Invalid input , Please try again")
            Application.continuation()             


obj= Application()
obj.start()
