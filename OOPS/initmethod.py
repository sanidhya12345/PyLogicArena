class Initmethod:
    def __init__(self,name):
        self.name=name
    
    def printmyname(self):
        print(f"Hey this is {self.name}")
    

name=input('Enter your name: ')
obj=Initmethod(name)
obj.printmyname()