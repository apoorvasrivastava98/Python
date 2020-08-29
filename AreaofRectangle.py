class Area:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def rectangle(self):
        return self.length * self.breadth

obj = Area(7,5)
print("Area of rectangle:", obj.rectangle())
