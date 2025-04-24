
class Pixel:
    truthy = "░XxO"
    falsy = " _-"
    def __init__(self, value):
        if value in self.truthy:
            self.value = True
        elif value in self.falsy:
            self.value = False
        else:
            raise ValueError(f"Connot interpret pixel '{value}' as on or off.")
    def __repr__(self):
        return self.truthy[0] if self.value else self.falsy[0]

class Column:
    def __init__(self, pixel_str):
        self.pixels = [Pixel(value) for value in pixel_str]
        self.pixels = tuple(self.pixels)
        self.height = len(self.pixels)
    def __repr__(self):
        chars = [str(pixel) for pixel in self.pixels]
        return "\n".join(chars)

class Character:
    def __init__(self, *columns):
        self.columns = columns
        heights = [column.height for column in self.columns]
        if max(heights) != min(heights):
            raise ValueError("Characters must all be of the same height.")
        self.height = heights[0]
    def __repr__(self):
        rows = []
        for row in range(self.height):
            rows.append("".join([str(column.pixels[row]) for column in self.columns]))
        return "\n".join(rows)
            
x = Column("x x x ")
y = Column("x x x ")
z = Column(" x x x")
c = Character(x,y,z)
print(x)
print(c)