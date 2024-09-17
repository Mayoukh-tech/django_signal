class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Define the __iter__ method to make the class iterable
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage
rectangle = Rectangle(length=10, width=5)

for dimension in rectangle:
    print(dimension)
