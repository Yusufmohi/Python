class room():
    advance="1000"
    def __init__(self,rent,sts):
        self.rent=rent
        self.status=sts
    def check(self):
        print("Rent:",self.rent)
        print("Status:",self.status)
    @classmethod
    def newadvance(cls):
        cls.advance="2000"
        print("Advance changed to 2000 from Today")
    @staticmethod
    def info():
        print("Pay the rent late,I'll Delay your wife Date")

room1=room(500,"Available")

room1.check()
room1.newadvance()
room1.info()
