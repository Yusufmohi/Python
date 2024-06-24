def function1(r1,r2):
    return r1+r2

r1=int(input("a:"))
r2=int(input("b:"))
r3=int(input("c:"))
e=function1(r1,r2)

def function2():
    return "your answer is" + str(e*r3)
f=function2()
print(f)
