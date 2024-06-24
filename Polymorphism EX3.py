class Vehicle():
    def start(self):
        print("Vehicle is Started")
class car(Vehicle):
    def start(self):
        print("Car is Started")
r1=car()
r1.start()
