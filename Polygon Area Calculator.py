import re


class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        self.perimeter = 2 * self.width + 2 * self.height
        return self.perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal


    def get_picture(self):
        if self.width>50 or self.height > 50:
            return "Too big for picture."
        else:
            string = ""
            cols = "*" * self.width
            rows = self.height
            for row in range(rows):
                string += cols + "\n"
        return string
    
    def get_amount_inside(self, obj):
    
        fits = (self.width * self.height) // (obj.width * obj.height)
        return fits


    def __str__(self) -> str:
        string = f'Rectangle(width={self.width}, height={self.height})'
        return string


class Square(Rectangle):
    def __init__(self, side) -> None:
        _side= side
        super(Square, self).__init__(_side, _side)
    
    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)
         
    def set_width(self, side):
        self.set_side(side)
    
    def set_height(self, side):
        self.set_side(side)
    
    def __str__(self) -> str:
        string = f'Square(side={self.width})'
        return string



    
    

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)

print(rect.get_amount_inside(sq))
