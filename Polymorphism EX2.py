class Person():
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def show(self):
        print("Name:",self.name)
        print("Grade:",self.grade)

g1=Student("Sohail","A+")
g1.show()
