a=[]
print("Enter 10 Numbers")
sum=0
Avg=0
for i in range(10):
    num=int(input("Enter Number:"+ str(i+1)))
    a.append(num)
    sum=sum+num
    Avg=sum/10
print(sum)
print(Avg)
