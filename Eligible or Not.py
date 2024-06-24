Score=int(input("Your percentage is:"))
if(Score>=70):
    Name=input("Name:")
    Dept=input("Dept:")
    Location=input("Location:")
    print("Eligible")
elif(Score<70):
    print("Not Eligible")
else:
    print("Invalid")
