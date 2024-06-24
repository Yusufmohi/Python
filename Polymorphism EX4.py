class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Manager(Employee):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept
    def show(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.dept)

w1=Manager("Tony",20000,"Mining")
w1.show()
