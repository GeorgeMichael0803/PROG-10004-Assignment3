from Building import Building
from SheridanSystem import SheridanSystem


class Application:
    def start():
        Building.buildingName()
        SheridanSystem.run()





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