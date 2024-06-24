class Animal():
    def sound(self):
        print("Animal Makes Sound")
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
class Bird(Animal):
    def sound(self):
        print("Bird Sings")

b1=Dog()
b1.sound()
b2=Bird()
b2.sound()
    
