from math import sqrt

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width) -> None:
        self.width = width

    def set_height(self, height) -> None:
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return sqrt(self.height ** 2 + self.width ** 2)

    def get_amount_inside(self, shape) -> int:
        return self.get_area() // shape.get_area()

    def get_picture(self):
        if self.width > 50 or self.height > 50:
        	return "Too big for picture."
        return( ( ("*" * self.width)+ "\n" ) * self.height)


class Square(Rectangle):
    def __init__(self, side, **kwargs):
        super().__init__(height=side, width=side, **kwargs)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)

    def set_height(self, height):
        super().set_width(height)
        super().set_height(height)
