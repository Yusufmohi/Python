class teacher:
    def __init__(self,nme,rtr):
        self.name=nme
        self.reg=rtr
    def show(self):
        print("Name:",self.name)
        print("Reg.",self.reg)

t1=teacher("Morty","1")
t2=teacher("David","2")

t1.show()
t2.show()
