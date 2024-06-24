class dad():
    def money(self):
        print("Dad's Money")
class mom(dad):
    def card(self):
        print("Mom's Card")
class son(mom):
    def fees(self):
        print("Deposit money")

sohail=son()
sohail.fees()
sohail.card()
sohail.money()
