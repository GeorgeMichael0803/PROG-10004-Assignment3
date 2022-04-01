


class SheridanSystem():
    def __init__(self,noOfBuild=0):
        self._nofBuildings = noOfBuild
           

    def run(self):
            try:
                self._nofBuildings= int(input("Enter the number of buildings: "))
            except ValueError:
                print("Invalid Entry")
                self._nofBuildings= int(input("Re-Enter the number of buildings [Numbers only]: ")) 
            if (self._nofBuildings <1):
                print("Invalid Entry")
                self._nofBuildings= int(input("Re-Enter the number of buildings [Positive Numbers only]: ")) 
            else:
                pass    


hello = SheridanSystem()
hello.run()        