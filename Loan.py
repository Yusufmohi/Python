Salary=int(input("Your salary:"))
age=int(input("Your Age:"))
if(Salary>=20000 or age<=25):
    print("You're Elgible")
    loan=int(input("Your Loan Amount:"))
    if(loan<=50000):
        print("Eligible for Loan and Congratulations")
    if(loan>50000):
         print("Max.Lon amt is 50000 Sorry")
else:
    print("Not Eligible")
