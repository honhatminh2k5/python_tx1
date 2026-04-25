class Shape:
    def __init__(self,color):
        self.color=color

    def draw(self):
        print(f"Dang ve 1 hcn co mau{self.color}")

class Rectangle(Shape):
    def __init__(self,color,width,height):
        super().__init__(color)
        self.width=width
        self.height=height

    def draw(self):
        print(f"Ve hcn co mau {self.color} va chieu rong {self.width} va chieu cao {self.height}")

hcn=Rectangle("do",10,20)
hcn.draw()