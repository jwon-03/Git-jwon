class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

class Rectangle:
    def __init__(self, left, top, right, bottom):
        self.lt = Point(left, top)
        self.rb = Point(right, bottom)

    def show(self):
        print(f'({self.lt.x}, {self.lt.y}), ({self.rb.x}, {self.rb.y})')

    def getWidth(self):#너비
        return self.rb.x - self.lt.x

    def getHeight(self):#높이
        return self.rb.y - self.lt.y

    def getArea(self):#넓이
        return (self.rb.x - self.lt.x) * (self.rb.y - self.lt.y)

    def getPerimeter(self):#둘레
        return 2 * (self.rb.x - self.lt.x) + 2 * (self.rb.y - self.lt.y)

#주프로그램부
    
r1 = Rectangle()
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
