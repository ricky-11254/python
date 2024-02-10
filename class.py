class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        rect_area = self.length * self.width
        return rect_area
rectangle1 = Rectangle(7, 5)
print(rectangle1.area())
