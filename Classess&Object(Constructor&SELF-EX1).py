class student:
    def __init__(self):
        name=""
        register=0
    def display(self):
        print("Name:",self.name)
        print("Register Number:",self.register)

thennuh=student()
gokul=student()
ramalingam=student()

thennuh.name="Thennarasi"
thennuh.register=38

gokul.name="Gokul"
gokul.register=7

ramalingam.name="Ramalingam"
ramalingam.register=29

thennuh.display()
gokul.display()
ramalingam.display()
