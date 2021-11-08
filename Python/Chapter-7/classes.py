# learning about classes and inheritence

class Car:
    def __init__(self, make, model,color):
        self.make = make
        self.model = model
        self.color = color
    
    def honk(self):
        print("honk!")
    
    def __str__(self):
        return(f"{self.color} {self.make} {self.model}")
    
class ClownCar(Car):
    def honk(self):
        print("beep beep beep")

pinto = Car("Ford", "Pinto", "Blue")

pinto.honk()
print(pinto)

gremlin = Car("AMC", "Gremlin", "Lime Green")

print(gremlin)
gremlin.honk()

clownCar = ClownCar("Mini", "Cooper", "Rainbow")

print(clownCar)
clownCar.honk()
