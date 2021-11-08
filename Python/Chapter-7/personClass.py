class Person:
    def __init__(self,fName, lName, age, gender):
        self.fName = fName
        self.lName = lName
        self.age = age
        self.gender = gender
    
    def __str__(self):
        definition = f"{self.fName} {self.lName}, a {self.age} year old "
        if self.gender == "M":
            definition += "male"
        else:
            definition += "female"
        return(definition)
    
    def fullName(self):
        print(f"{self.fName} {self.lName}")
    
    def title(self):
        if self.gender == "M":
            print("Mr.", self.fName, self.lName)
        else:
            print("Mrs.", self.fName, self.lName)


class Doctor(Person):
    def title(self):
        print("Doc.", self.fName, self.lName)

class Professor(Person):
    def title(self):
        print("Prof.", self.fName, self.lName)


Randall = Person("Randall", "Gosnell", 30, "M")
Jessy = Doctor("Jessy", "Smith", 20, "F")
Matt = Professor("Matt", "Smith", 53, "M")

print(Randall)
print(Jessy)
print(Matt)

Randall.title()
Jessy.title()
Matt.title()