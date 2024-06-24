class a():
    def __init__(self):
        print("A")
    def show(self):
        print("This is A")
class b(a):
    def __init__(self):
        super().__init__()
        print("B")
    def show(self):
        print("This is B")
class c(b,a):
    def __init__(self):
        super().__init__()
        print("C")
    def show(self):
        print("This is C")

r1=c()
r1.show()
