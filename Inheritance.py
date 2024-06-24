class dad():
    def phone(self):
        print("Dad's Phone")

class mom():
    def sweet(self):
        print("Mom's Sweet")

class son(mom,dad):
    def laptop(self):
        print("My Laptop")

sohail=son()
sohail.laptop()
sohail.sweet()
sohail.phone()
