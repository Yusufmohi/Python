class cal:
   def  __init__(self,x,y):
        self.a=x
        self.b=y
   def sum(self):
        print(self.a+self.b)
   def sub(self):
        print(self.a-self.b)
   def mul(self):
        print(self.a*self.b)
   def div(self):
        print(self.a/self.b)

    
v1=cal(int(input()),int(input()))

v1.mul()
v1.sum()
v1.sub()
v1.div()
