class Shape():
    def area(self):
        return 0
class Rectangle(Shape):
    def area(self):
        l=int(input())
        b=int(input())
        return l*b
    
s1=Rectangle()
print(s1.area())
