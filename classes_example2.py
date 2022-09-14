class Rectangle:
    def __init__(self, w,l):
        self.width = w
        self.length =l
    def rectangle_area(self):
        return self.width*self.length

myRectangle=Rectangle(2,9)
print(myRectangle.rectangle_area())

class Circle :
    def __init__(self, r):
        self.radius =r
    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return self.radius*2*3.14

circle=Circle(8)
print(circle.area())
print(circle.perimeter())
