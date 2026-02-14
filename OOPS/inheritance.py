#Parent Class
class Person:

    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    
    def printname(self):
        print(self.firstname,self.lastname)

#Student Class
class Student(Person):

    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduation_year=year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduation_year)
#if we write the init function inside the child class it will overrides the parent init function
#so to avoid this we have to call the parent init function



x=Student("sanidhya","varshney",2023)
x.welcome()