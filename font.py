from api import display_character

zero_width_joiner = "‍"

def transpose(lists):
    result = []
    for x in range(len(lists[0])):
        result.append([l[x] for l in lists])
    return result

class Pixel:
    truthy = "•○░XxO"
    falsy = " _-"
    def __init__(self, value):
        if value in self.truthy:
            self.value = True
        elif value in self.falsy:
            self.value = False
        else:
            raise ValueError(f"Connot interpret pixel '{value}' as on or off.")
    def __bool__(self):
        return self.value
    def __repr__(self):
        return self.truthy[0] if self.value else self.falsy[0]

class Column:
    def __init__(self, pixel_str):
        self.pixels = [Pixel(value) for value in pixel_str]
        self.pixels = tuple(self.pixels)
        self.height = len(self.pixels)
    def __getitem__(self, index):
        return self.pixels.__getitem__(index)
    def __len__(self):
        return len(self.pixels)
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
    def __getitem__(self, index):
        return self.columns.__getitem__(index)
    def __add__(self, other):
        return Character(*(self.columns + other.columns))
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
    def __len__(self):
        return len(self.columns)
    def __repr__(self):
        rows = transpose(self.columns)
        return rows_to_str(rows)
    
class Font:
    def __init__(self, characters):
        self.characters = characters
    def convert(self, text):
        text = zero_width_joiner.join(text)
        characters = [self.characters.get(c) for c in text]
        return sum(characters)
    def print(self, text):
        representation = self.convert(text)
        rows = transpose(representation)
        print(rows_to_str(rows))
    def display(self, text):
        representation = self.convert(text)
        display_character(representation)

def rows_to_str(rows):
    return "\n".join(["".join(map(str, pixel)) for pixel in rows])