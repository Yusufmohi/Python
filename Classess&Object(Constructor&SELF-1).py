class laptop:
    def __init__(self):
        price=0
        ram=""
    def display(self):
        print("Price:",self.price)
        print("Ram:",self.ram)

hp=laptop()
dell=laptop()

hp.price=50000
dell.price=30000

hp.ram="i5"
dell.ram="i3"

hp.display()
dell.display()
        
